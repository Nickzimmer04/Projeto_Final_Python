from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import PokemonBase, PokemonUpdate
from app.database import get_db
from app.models import Pokemon
from app.pokeapi import get_pokemon

from app.services.pokemon_service import (
    create_pokemon as create_pokemon_service,
    get_pokemon_by_id as get_pokemon_by_id_service,
    list_pokemons as list_pokemons_service,
    update_pokemon as update_pokemon_service,
    delete_pokemon as delete_pokemon_service
)

router = APIRouter()



@router.get("/pokemon")
def list_pokemon(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    pokemons = list_pokemons_service(db, skip, limit)
    return pokemons

@router.get("/pokemon/id/{pokemon_id}")
def get_pokemon_by_id(pokemon_id: int, db: Session = Depends(get_db)):
    pokemon = get_pokemon_by_id_service(pokemon_id, db)

    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado")

    return pokemon

@router.get("/pokemon/{name}")
def read_pokemon(name: str):
    pokemon = get_pokemon(name)

    if "error" in pokemon:
        raise HTTPException(
            status_code=404,
            detail=pokemon["error"]
    )

    return pokemon

@router.post("/pokemon")
def create_pokemon(pokemon: PokemonBase, db: Session = Depends(get_db)):

    new_pokemon = Pokemon(
        name=pokemon.name,
        type=pokemon.type,
        level=pokemon.level
    )
    try:
        created_pokemon = create_pokemon_service(new_pokemon, db)

        return {
            "message": f"Pokémon {created_pokemon.name} criado com sucesso!",
            "pokemon": created_pokemon
        }
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    
@router.put("/pokemon/{pokemon_id}")
def update_pokemon(pokemon_id: int, pokemon: PokemonUpdate, db: Session = Depends(get_db)):
    try:
        updated_pokemon = update_pokemon_service(pokemon_id, pokemon, db)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

    if not updated_pokemon:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado")

    return {"message": f"Pokémon {updated_pokemon.name} atualizado com sucesso!"}
    

@router.delete("/pokemon/{pokemon_id}")
def delete_pokemon(pokemon_id: int, db: Session = Depends(get_db)):
    deleted_pokemon = delete_pokemon_service(pokemon_id, db)

    if not deleted_pokemon:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado")

    return {
        "message": f"Pokémon {deleted_pokemon} deletado com sucesso!"
    }