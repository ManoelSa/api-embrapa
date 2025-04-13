from fastapi import FastAPI
from app.router import embrapa
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

app = FastAPI(
    title="API Embrapa",
    version="1.0.0",
    description="API Para Fins de Estudus - FIAP"
)

app.include_router(embrapa.router)