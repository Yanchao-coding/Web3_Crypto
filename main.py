from fastapi import FastAPI
from modules.core.router import router

app = FastAPI()
app.include_router(router)
