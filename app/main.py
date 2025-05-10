from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from app.router import embrapa
from app.config import security
from app.handlers.validation import validation_handler

app = FastAPI(
    title="API Embrapa - 2025",
    version="1.0.0",
    description="API Para Fins de Estudus - FIAP"
)

app.add_exception_handler(RequestValidationError, validation_handler)

app.include_router(embrapa.router)
app.include_router(security.router)