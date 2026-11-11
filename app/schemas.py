from pydantic import BaseModel

class PokemonBase(BaseModel):
    name: str
    type: str
    level: int