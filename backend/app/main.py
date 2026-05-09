from fastapi import FastAPI
from app.api.v1.routes import router as v1_router

app = FastAPI(title="BrandIntelligence", version="0.1.0")
app.include_router(v1_router, prefix="/v1")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
