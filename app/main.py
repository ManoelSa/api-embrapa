from fastapi import FastAPI
from router import embrapa

app = FastAPI(
    title="API Embrapa",
    version="1.0.0",
    description="API Para Fins de Estudus - FIAP"
)

app.include_router(embrapa.router)