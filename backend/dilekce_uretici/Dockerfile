### dilekce_uretici/backend/dilekce_uretici/app.py
from fastapi import FastAPI

app = FastAPI()

# ------------------------------------------------------------------
# Health-check endpoints
@app.get("/health")
@app.get("/api/health")
def health():
    return {"status": "ok"}
# ------------------------------------------------------------------

# ... rest of the file ...