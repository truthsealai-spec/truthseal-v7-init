 # Local dry-run (no network): prints one Prometheus line without pushing
python -c "from governance.guards.observability.metrics_transmitter_v1 import MetricsTransmitter; tx=MetricsTransmitter('https://example.invalid','user','token','hmac','pin'); print(tx._format_metric('Red_Line_Trip_Count',1.0,{'source':'selftest','instance':'local','job':'truthseal_security_reporter'}))"
