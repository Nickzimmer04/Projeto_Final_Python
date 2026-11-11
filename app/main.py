from fastapi import FastAPI
from app.schemas import PokemonBase

app = FastAPI(
    title = "Pokedex API - Projeto final"
    )

@app.get("/health")
def health_check():
    return {"status": "online"}

@app.get("/")
def get_message():
    return {"message": "Boas-vindas à API!"}

@app.post("/pokemon")
def create_pokemon(pokemon: PokemonBase):
    return {"message": f"Pokémon {pokemon.name} do tipo {pokemon.type} de nível {pokemon.level} criado com sucesso!"}
