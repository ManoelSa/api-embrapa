from fastapi import FastAPI
from app.router import embrapa
from app.config import security

app = FastAPI(
    title="API Embrapa - 2025",
    version="1.0.0",
    description="API Para Fins de Estudus - FIAP"
)

app.include_router(embrapa.router)
app.include_router(security.router)