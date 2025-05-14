# app/main.py

from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.routes import router
from app.services import service

@asynccontextmanager
async def lifespan(app: FastAPI):
    # aquí se carga el embedder, el índice y el engine
    service.load_model()
    yield
    # (aquí podrías liberar recursos si hiciera falta)

def create_app() -> FastAPI:
    app = FastAPI(title="RAG Chatbot API", lifespan=lifespan)
    app.include_router(router)
    return app

app = create_app()
