from fastapi import FastAPI, Depends, HTTPException
from app.schemas import PokemonBase
from app.database import Base, engine, get_db
from app.models import Pokemon
from sqlalchemy.orm import Session
from app.pokeapi import get_pokemon


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

@app.get("/pokemon")
def list_pokemon(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    pokemons = db.query(Pokemon).offset(skip).limit(limit).all()
    return pokemons

@app.get("/pokemon/id/{pokemon_id}")
def get_pokemon_by_id(pokemon_id: int, db: Session = Depends(get_db)):
    pokemon = db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado")
    return pokemon

@app.get("/pokemon/{name}")
def read_pokemon(name: str):
    pokemon = get_pokemon(name)

    if "error" in pokemon:
        raise HTTPException(
            status_code=404,
            detail=pokemon["error"]
    )

    return pokemon
    

@app.post("/pokemon")
def create_pokemon(pokemon: PokemonBase, db: Session = Depends(get_db)):

    # Verifica se já existe um Pokémon com o mesmo nome
    existing_pokemon = db.query(Pokemon).filter(
        Pokemon.name == pokemon.name
    ).first()

    if existing_pokemon:
        raise HTTPException(
            status_code=409,
            detail=f"Pokémon com o nome '{pokemon.name}' já existe."
        )

    # Cria o objeto somente se não houver duplicidade
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
