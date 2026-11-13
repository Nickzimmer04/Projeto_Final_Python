from fastapi import FastAPI, Depends
from app.schemas import PokemonBase
from app.database import Base, engine, get_db
from app.models import Pokemon
from fastapi import Depends
from sqlalchemy.orm import Session


app = FastAPI(
    title = "Pokedex API - Projeto final"
    )

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "online"}

@app.get("/")
def get_message():
    return {"message": "Boas-vindas à API!"}

@app.post("/pokemon")
def create_pokemon(pokemon: PokemonBase, db: Session = Depends(get_db)):

    db_pokemon = Pokemon(
        name=pokemon.name,
        type=pokemon.type,
        level=pokemon.level
    )

    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)

    return {
        "message": f"Pokémon {db_pokemon.name} do tipo {db_pokemon.type} de nível {db_pokemon.level} criado com sucesso!"
    }