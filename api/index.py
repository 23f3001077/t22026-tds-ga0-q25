from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json, numpy as np, os

app = FastAPI()

# CORS fix — allow POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the telemetry JSON (bundled in the repo)
DATA_PATH = os.path.join(os.path.dirname(__file__), "q-vercel-latency.json")
with open(DATA_PATH) as f:
    RAW = json.load(f)

@app.post("/")
async def analytics(request: Request):
    body = await request.json()
    regions   = body.get("regions", [])
    threshold = body.get("threshold_ms", 0)

    result = {}
    for region in regions:
        rows = [r for r in RAW if r["region"] == region]
        if not rows:
            result[region] = {}
            continue
        latencies = [r["latency_ms"] for r in rows]
        uptimes   = [r["uptime_pct"] for r in rows]
        result[region] = {
            "avg_latency": round(float(np.mean(latencies)), 4),
            "p95_latency": round(float(np.percentile(latencies, 95)), 4),
            "avg_uptime":  round(float(np.mean(uptimes)), 4),
            "breaches":    int(sum(1 for l in latencies if l > threshold)),
        }
    return JSONResponse(result)
