from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json, numpy as np, os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

DATA_PATH = os.path.join(os.path.dirname(__file__), "q-vercel-latency.json")
with open(DATA_PATH) as f:
    RAW = json.load(f)

# Explicit OPTIONS handler so Vercel doesn't swallow the preflight
@app.options("/")
async def options_root():
    return JSONResponse(
        content={},
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "*",
        },
    )

@app.post("/")
async def analytics(request: Request):
    body      = await request.json()
    regions   = body.get("regions", [])
    threshold = body.get("threshold_ms", 0)

    result = {}
    for region in regions:
        rows = [r for r in RAW if r["region"] == region]
        if not rows:
            result[region] = {}
            continue
        latencies = [r["latency_ms"] for r in rows]
        uptimes   = [r["uptime_pct"]  for r in rows]
        result[region] = {
            "avg_latency": round(float(np.mean(latencies)),        4),
            "p95_latency": round(float(np.percentile(latencies, 95)), 4),
            "avg_uptime":  round(float(np.mean(uptimes)),          4),
            "breaches":    int(sum(1 for l in latencies if l > threshold)),
        }

    return JSONResponse(
        content=result,
        headers={"Access-Control-Allow-Origin": "*"},
    )
