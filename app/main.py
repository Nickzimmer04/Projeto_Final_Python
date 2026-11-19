import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.database import Base, engine
from app.routers.pokemon import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    if os.getenv("TESTING") != "1":
        Base.metadata.create_all(bind=engine)

    yield


app = FastAPI(
    title="Pokedex API - Projeto final",
    lifespan=lifespan
)

app.include_router(router)


@app.get("/health")
def health_check():
    return {"status": "online"}


@app.get("/")
def get_message():
    return {"message": "Boas-vindas à API!"}
