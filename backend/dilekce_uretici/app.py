from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# ------------------------------------------------------------------
# Health-check endpoints for liveness/readiness probes
@app.get("/health")
@app.get("/api/health")
def health():
    return {"status": "ok"}
# ------------------------------------------------------------------

class PetitionRequest(BaseModel):
    name: str
    tc: str
    subject: str

@app.post("/api/petition")
def create_petition(req: PetitionRequest):
    return {
        "petition": f"Dilekçe taslağı — Başvurucu: {req.name} — Konu: {req.subject}"
    }