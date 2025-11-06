import os
from base64 import b64encode, b64decode
from typing import Tuple, Dict
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.hashes import SHA3_256
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from kyber_py.ml_kem import ML_KEM_768  # ensure this is the NIST ML-KEM impl

NONCE_SIZE = 12  # GCM standard
AES_KEY_LEN = 32  # 256-bit

class TruthSealPQC:
    """KEM-DEM hybrid: ML-KEM-768 for key encapsulation + AES-256-GCM for AEAD DEM."""

    @staticmethod
    def generate_keypair() -> Tuple[bytes, bytes]:
        return ML_KEM_768.keygen()  # (public_key, private_key)

    @staticmethod
    def _derive_aes_key(shared_secret: bytes, kem_ct: bytes) -> bytes:
        # salt binds the KDF to the exact KEM ciphertext; info binds to app context
        hkdf = HKDF(algorithm=SHA3_256(), length=AES_KEY_LEN,
                    salt=kem_ct, info=b"TruthSeal KEM-DEM v1")
        return hkdf.derive(shared_secret)

    @staticmethod
    def hybrid_encrypt(plaintext: bytes, receiver_pk: bytes,
                       aad: bytes = b"") -> Dict[str, str]:
        # 1) KEM
        kem_ct, ss = ML_KEM_768.encaps(receiver_pk)          # standard API
        aes_key = TruthSealPQC._derive_aes_key(ss, kem_ct)
        # 2) DEM (AEAD)
        nonce = os.urandom(NONCE_SIZE)
        aesgcm = AESGCM(aes_key)
        ciphertext = aesgcm.encrypt(nonce, plaintext, aad)   # tag included
        return {
            "ciphertext": b64encode(ciphertext).decode(),
            "nonce": b64encode(nonce).decode(),
            "kem_ct": b64encode(kem_ct).decode(),
            "aad": b64encode(aad).decode()
        }

    @staticmethod
    def hybrid_decrypt(encrypted: Dict[str, str], receiver_sk: bytes) -> bytes:
        kem_ct = b64decode(encrypted["kem_ct"])
        nonce = b64decode(encrypted["nonce"])
        ciphertext = b64decode(encrypted["ciphertext"])
        aad = b64decode(encrypted.get("aad",""))
        # 1) KEM
        ss = ML_KEM_768.decaps(receiver_sk, kem_ct)
        aes_key = TruthSealPQC._derive_aes_key(ss, kem_ct)
        # 2) DEM (AEAD)
        aesgcm = AESGCM(aes_key)
        return aesgcm.decrypt(nonce, ciphertext, aad)
