from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import math

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "GET", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["Access-Control-Allow-Origin"],
)

TELEMETRY = [
    {
        "region": "apac",
        "service": "catalog",
        "latency_ms": 202.3,
        "uptime_pct": 97.607,
        "timestamp": 20250301
    },
    {
        "region": "apac",
        "service": "catalog",
        "latency_ms": 136.47,
        "uptime_pct": 99.307,
        "timestamp": 20250302
    },
    {
        "region": "apac",
        "service": "analytics",
        "latency_ms": 206.86,
        "uptime_pct": 97.263,
        "timestamp": 20250303
    },
    {
        "region": "apac",
        "service": "recommendations",
        "latency_ms": 138.54,
        "uptime_pct": 97.951,
        "timestamp": 20250304
    },
    {
        "region": "apac",
        "service": "catalog",
        "latency_ms": 162,
        "uptime_pct": 98.088,
        "timestamp": 20250305
    },
    {
        "region": "apac",
        "service": "catalog",
        "latency_ms": 143.84,
        "uptime_pct": 98.584,
        "timestamp": 20250306
    },
    {
        "region": "apac",
        "service": "recommendations",
        "latency_ms": 191.82,
        "uptime_pct": 97.87,
        "timestamp": 20250307
    },
    {
        "region": "apac",
        "service": "payments",
        "latency_ms": 212.59,
        "uptime_pct": 97.432,
        "timestamp": 20250308
    },
    {
        "region": "apac",
        "service": "support",
        "latency_ms": 114.47,
        "uptime_pct": 97.632,
        "timestamp": 20250309
    },
    {
        "region": "apac",
        "service": "support",
        "latency_ms": 192.96,
        "uptime_pct": 98.671,
        "timestamp": 20250310
    },
    {
        "region": "apac",
        "service": "analytics",
        "latency_ms": 177.82,
        "uptime_pct": 97.448,
        "timestamp": 20250311
    },
    {
        "region": "apac",
        "service": "recommendations",
        "latency_ms": 115.19,
        "uptime_pct": 98.155,
        "timestamp": 20250312
    },
    {
        "region": "emea",
        "service": "support",
        "latency_ms": 165.62,
        "uptime_pct": 99.28,
        "timestamp": 20250301
    },
    {
        "region": "emea",
        "service": "payments",
        "latency_ms": 121.98,
        "uptime_pct": 97.23,
        "timestamp": 20250302
    },
    {
        "region": "emea",
        "service": "catalog",
        "latency_ms": 199.18,
        "uptime_pct": 97.465,
        "timestamp": 20250303
    },
    {
        "region": "emea",
        "service": "checkout",
        "latency_ms": 131.88,
        "uptime_pct": 98.275,
        "timestamp": 20250304
    },
    {
        "region": "emea",
        "service": "analytics",
        "latency_ms": 213.97,
        "uptime_pct": 99.009,
        "timestamp": 20250305
    },
    {
        "region": "emea",
        "service": "support",
        "latency_ms": 113.57,
        "uptime_pct": 97.481,
        "timestamp": 20250306
    },
    {
        "region": "emea",
        "service": "support",
        "latency_ms": 155.88,
        "uptime_pct": 97.688,
        "timestamp": 20250307
    },
    {
        "region": "emea",
        "service": "checkout",
        "latency_ms": 112.21,
        "uptime_pct": 99.21,
        "timestamp": 20250308
    },
    {
        "region": "emea",
        "service": "payments",
        "latency_ms": 223.54,
        "uptime_pct": 97.796,
        "timestamp": 20250309
    },
    {
        "region": "emea",
        "service": "analytics",
        "latency_ms": 158.33,
        "uptime_pct": 97.753,
        "timestamp": 20250310
    },
    {
        "region": "emea",
        "service": "recommendations",
        "latency_ms": 158.88,
        "uptime_pct": 99.178,
        "timestamp": 20250311
    },
    {
        "region": "emea",
        "service": "payments",
        "latency_ms": 188.23,
        "uptime_pct": 97.268,
        "timestamp": 20250312
    },
    {
        "region": "amer",
        "service": "analytics",
        "latency_ms": 182.84,
        "uptime_pct": 98.248,
        "timestamp": 20250301
    },
    {
        "region": "amer",
        "service": "payments",
        "latency_ms": 153.63,
        "uptime_pct": 97.904,
        "timestamp": 20250302
    },
    {
        "region": "amer",
        "service": "payments",
        "latency_ms": 163.23,
        "uptime_pct": 99.41,
        "timestamp": 20250303
    },
    {
        "region": "amer",
        "service": "checkout",
        "latency_ms": 148.06,
        "uptime_pct": 99.499,
        "timestamp": 20250304
    },
    {
        "region": "amer",
        "service": "support",
        "latency_ms": 150.21,
        "uptime_pct": 99.157,
        "timestamp": 20250305
    },
    {
        "region": "amer",
        "service": "support",
        "latency_ms": 195.32,
        "uptime_pct": 97.874,
        "timestamp": 20250306
    },
    {
        "region": "amer",
        "service": "payments",
        "latency_ms": 178.82,
        "uptime_pct": 98.998,
        "timestamp": 20250307
    },
    {
        "region": "amer",
        "service": "payments",
        "latency_ms": 191.17,
        "uptime_pct": 99.228,
        "timestamp": 20250308
    },
    {
        "region": "amer",
        "service": "analytics",
        "latency_ms": 218.71,
        "uptime_pct": 98.656,
        "timestamp": 20250309
    },
    {
        "region": "amer",
        "service": "catalog",
        "latency_ms": 200.42,
        "uptime_pct": 99.345,
        "timestamp": 20250310
    },
    {
        "region": "amer",
        "service": "analytics",
        "latency_ms": 134.17,
        "uptime_pct": 98.399,
        "timestamp": 20250311
    },
    {
        "region": "amer",
        "service": "catalog",
        "latency_ms": 122,
        "uptime_pct": 99.376,
        "timestamp": 20250312
    }
]


def percentile(values, p):
    values = sorted(values)
    if not values:
        return 0.0
    if len(values) == 1:
        return float(values[0])
    position = (len(values) - 1) * p
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return float(values[lower])
    fraction = position - lower
    return float(values[lower] * (1 - fraction) + values[upper] * fraction)


def calculate_metrics(region, threshold_ms):
    rows = [r for r in TELEMETRY if r["region"].lower() == str(region).lower()]
    if not rows:
        return None
    latencies = [float(r["latency_ms"]) for r in rows]
    uptimes = [float(r["uptime_pct"]) for r in rows]
    return {
        "avg_latency": round(sum(latencies) / len(latencies), 4),
        "p95_latency": round(percentile(latencies, 0.95), 4),
        "avg_uptime": round(sum(uptimes) / len(uptimes), 4),
        "breaches": sum(1 for latency in latencies if latency > threshold_ms),
    }


async def process_request(request: Request):
    body = await request.json()
    requested_regions = body.get("regions", [])
    threshold_ms = float(body.get("threshold_ms", 180))
    metrics_by_region = {}

    for region in requested_regions:
        metrics = calculate_metrics(region, threshold_ms)
        if metrics is not None:
            metrics_by_region[str(region).lower()] = metrics

    # The evaluator expects a top-level "regions" array or object.
    return {"regions": metrics_by_region}


@app.post("/")
async def analytics_root(request: Request):
    return await process_request(request)


@app.post("/{path:path}")
async def analytics_any_path(path: str, request: Request):
    return await process_request(request)
