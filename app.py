#  2026 Julius Cameron Hill / TitanU AI LLC. All rights reserved. Patent pending JCH-2026-001.
from fastapi import FastAPI
from agent import ReleaseTrainConductorAgent

app = FastAPI(title="TitanU - Release-Train-Conductor")
agent = ReleaseTrainConductorAgent()

@app.post("/execute")
async def execute(payload: dict):
    return agent.execute(payload)
