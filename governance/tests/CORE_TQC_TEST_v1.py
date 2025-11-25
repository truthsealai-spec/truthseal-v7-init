#!/usr/bin/env python3
# CORE_TQC_TEST_v1.py — Coherence stress test across Milvus (GPU) and pgvector
# Outputs a JSON summary under governance/ledger/receipts/benchmarks/

import os, sys, time, json, math, hashlib, random, datetime as dt
from statistics import mean
import numpy as np

# --- Milvus ---
from pymilvus import connections, utility, Collection
# --- Postgres / pgvector ---
import psycopg2

# ---------- Config (env or sensible defaults) ----------
MILVUS_HOST = os.getenv("MILVUS_HOST", "127.0.0.1")
MILVUS_PORT = int(os.getenv("MILVUS_PORT", "19530"))
MILVUS_COLLECTION = os.getenv("MILVUS_COLLECTION", "podapar_vectors")
MILVUS_VECTOR_FIELD = os.getenv("MILVUS_VECTOR_FIELD", "embedding")

PG_HOST = os.getenv("PG_HOST", "127.0.0.1")
PG_PORT = int(os.getenv("PG_PORT", "5432"))
PG_DB   = os.getenv("POSTGRES_DB", "api")
PG_USER = os.getenv("POSTGRES_USER", "postgres")
PG_PASS = os.getenv("POSTGRES_PASSWORD", "password")
PG_TABLE = os.getenv("PGVECTOR_TABLE", "podapar_embeddings")
PG_COL   = os.getenv("PGVECTOR_COL", "embedding")

N = int(os.getenv("CORE_TQC_N", "10000"))  # number of query vectors
TOPK = 1
COSINE = "COSINE"

out_dir = "governance/ledger/receipts/benchmarks/"
os.makedirs(out_dir, exist_ok=True)

def iso_now():
    return dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

def connect_milvus():
    connections.connect("default", host=MILVUS_HOST, port=MILVUS_PORT)
    if not utility.has_collection(MILVUS_COLLECTION):
        raise RuntimeError(f"Milvus collection not found: {MILVUS_COLLECTION}")
    return Collection(MILVUS_COLLECTION)

def connect_pg():
    conn = psycopg2.connect(
        host=PG_HOST, port=PG_PORT, dbname=PG_DB, user=PG_USER, password=PG_PASS
    )
    conn.autocommit = True
    return conn

def get_dims_from_milvus(col: Collection):
    return col.schema[MILVUS_VECTOR_FIELD].params["dim"]

def get_dims_from_pg(conn):
    with conn.cursor() as cur:
        cur.execute(f"SELECT vector_dims({PG_COL}) FROM {PG_TABLE} LIMIT 1;")
        row = cur.fetchone()
        if not row or not row[0]:
            raise RuntimeError("Cannot infer pgvector dimension. Ensure table has data.")
        return int(row[0])

def rand_unit_vectors(d, count):
    x = np.random.normal(size=(count, d)).astype("float32")
    norms = np.linalg.norm(x, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    return (x / norms).tolist()

def pg_top1_similarity(conn, qvec):
    # cosine distance operator in pgvector is "<=>"; similarity = 1 - distance
    qtxt = "[" + ",".join(f"{v:.6f}" for v in qvec) + "]"
    sql = f"""
      SELECT 1 - ({PG_COL} <=> %s) AS sim
      FROM {PG_TABLE}
      ORDER BY {PG_COL} <=> %s
      LIMIT 1;
    """
    with conn.cursor() as cur:
        cur.execute(sql, (qtxt, qtxt))
        row = cur.fetchone()
        return float(row[0]) if row else 0.0

def milvus_top1_similarity(col: Collection, qvec):
    res = col.search(
        data=[qvec],
        anns_field=MILVUS_VECTOR_FIELD,
        param={"metric_type": COSINE, "params": {"nprobe": 16}},
        limit=TOPK,
        output_fields=[]
    )
    # Milvus returns distance; for COSINE it is 1 - cosine_similarity
    d = float(res[0][0].distance)
    return 1.0 - d

def main():
    started = iso_now()
    col = connect_milvus()
    pg = connect_pg()

    d_m = get_dims_from_milvus(col)
    d_p = get_dims_from_pg(pg)
    if d_m != d_p:
        raise RuntimeError(f"Dim mismatch Milvus({d_m}) vs pgvector({d_p}).")

    queries = rand_unit_vectors(d_m, N)

    milvus_sims, pg_sims, diffs = [], [], []
    t_m, t_p = [], []

    for q in queries:
        t0 = time.perf_counter()
        sm = milvus_top1_similarity(col, q)
        t_m.append((time.perf_counter() - t0) * 1000.0)

        t1 = time.perf_counter()
        sp = pg_top1_similarity(pg, q)
        t_p.append((time.perf_counter() - t1) * 1000.0)

        milvus_sims.append(sm)
        pg_sims.append(sp)
        diffs.append(abs(sm - sp))

    report = {
        "test": "CORE_TQC_TEST_v1",
        "created_utc": started,
        "count": N,
        "dim": d_m,
        "milvus_collection": MILVUS_COLLECTION,
        "pg_table": PG_TABLE,
        "metrics": {
            "pscore_max_dev": max(diffs),
            "pscore_mean_dev": mean(diffs),
            "latency_ms": {
                "milvus_avg": mean(t_m),
                "pgvector_avg": mean(t_p)
            }
        },
        "pass_thresholds": {
            "pscore_max_dev_lt": 0.001
        },
        "pass": (max(diffs) < 0.001)
    }

    # write summary
    fname = f"{dt.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}__CORE_TQC_TEST_v1__summary.json"
    fpath = os.path.join(out_dir, fname)
    with open(fpath, "w") as f:
        json.dump(report, f, indent=2)

    print(f"Summary written: {fpath}")
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
