from fastapi import FastAPI
from router import get_producao
app = FastAPI()

app.include_router(get_producao.router)