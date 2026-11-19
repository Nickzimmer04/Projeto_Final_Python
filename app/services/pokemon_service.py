
from sqlalchemy.orm import Session
from app.models import Pokemon
from app.schemas import PokemonUpdate


def get_existing_pokemon(name: str, db: Session):
    # Filtrar o Pokémon pela tabela do banco de dados
    pokemon = db.query(Pokemon).filter(Pokemon.name == name).first()
    return pokemon


def create_pokemon(pokemon: Pokemon, db: Session):
    existing_pokemon = get_existing_pokemon(pokemon.name, db)

    if existing_pokemon:
        raise ValueError(f"Pokémon com o nome '{pokemon.name}' já existe.")

    db.add(pokemon)
    db.commit()
    db.refresh(pokemon)

    return pokemon


def get_pokemon_by_id(pokemon_id: int, db: Session):
    pokemon = db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()
    return pokemon


def list_pokemons(db: Session, skip: int = 0, limit: int = 10):
    pokemons = db.query(Pokemon).offset(skip).limit(limit).all()
    return pokemons


def update_pokemon(pokemon_id: int, pokemon_data: PokemonUpdate, db: Session):
    db_pokemon = db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()

    # Verificar se o Pokémon existe
    if not db_pokemon:
        return None

    if pokemon_data.name is not None:
        existing_pokemon = get_existing_pokemon(pokemon_data.name, db)

        if existing_pokemon and existing_pokemon.id != pokemon_id:
            raise ValueError(f"Pokémon com o nome '{pokemon_data.name}' já existe.")

    if pokemon_data.name is not None:
        db_pokemon.name = pokemon_data.name

    if pokemon_data.type is not None:
        db_pokemon.type = pokemon_data.type

    if pokemon_data.level is not None:
        db_pokemon.level = pokemon_data.level

    db.commit()
    db.refresh(db_pokemon)

    return db_pokemon


def delete_pokemon(pokemon_id: int, db: Session):
    db_pokemon = db.query(Pokemon).filter(Pokemon.id == pokemon_id).first()

    if not db_pokemon:
        return None

    pokemon_name = db_pokemon.name

    db.delete(db_pokemon)
    db.commit()

    return pokemon_name
