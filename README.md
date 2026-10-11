# Vercel POST Analytics Endpoint

The supplied telemetry records are embedded in `api/index.py`, so the function does not need to read a local data file at runtime.

## Test the deployment

```bash
curl -X POST 'https://YOUR-DEPLOYMENT-URL/' \
  -H 'Content-Type: application/json' \
  -d '{"regions":["emea","apac"],"threshold_ms":189}'
```

The response is a JSON object keyed by region. Breaches counts records whose latency is strictly greater than the threshold.
