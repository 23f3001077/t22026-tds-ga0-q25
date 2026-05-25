from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 210.45,
    "uptime_pct": 97.496,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 215.61,
    "uptime_pct": 98.177,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 225.78,
    "uptime_pct": 98.862,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 194.65,
    "uptime_pct": 97.605,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 154.22,
    "uptime_pct": 97.389,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 150.22,
    "uptime_pct": 98.642,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 232.29,
    "uptime_pct": 98.973,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 114.63,
    "uptime_pct": 98.742,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 179.62,
    "uptime_pct": 99.068,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 112.95,
    "uptime_pct": 99.478,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 212.07,
    "uptime_pct": 99.084,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 124.32,
    "uptime_pct": 98.167,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 121.73,
    "uptime_pct": 97.816,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 210.16,
    "uptime_pct": 99.019,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 138.77,
    "uptime_pct": 98.94,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 138.27,
    "uptime_pct": 99.16,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 202.19,
    "uptime_pct": 99.494,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 221.56,
    "uptime_pct": 99.37,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 136.62,
    "uptime_pct": 98.48,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 168.99,
    "uptime_pct": 98.608,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 181.4,
    "uptime_pct": 97.318,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 133.63,
    "uptime_pct": 98.899,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 116.12,
    "uptime_pct": 98.291,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 213.5,
    "uptime_pct": 97.584,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 227.9,
    "uptime_pct": 99.124,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 154.35,
    "uptime_pct": 97.871,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 134.61,
    "uptime_pct": 97.729,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 231.43,
    "uptime_pct": 97.331,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 211.98,
    "uptime_pct": 99.29,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 178.64,
    "uptime_pct": 98.403,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 202.45,
    "uptime_pct": 98.569,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 168.77,
    "uptime_pct": 98.735,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 177.3,
    "uptime_pct": 98.826,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 182.78,
    "uptime_pct": 99.294,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 158.21,
    "uptime_pct": 98.001,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 199.6,
    "uptime_pct": 98.145,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
