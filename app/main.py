from fastapi import FastAPI
from router import embrapa
app = FastAPI()

app.include_router(embrapa.router)