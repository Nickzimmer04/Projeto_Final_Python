from pydantic import BaseModel

class PokemonBase(BaseModel):
    name: str
    type: str
    level: int
# Permitir que os campos sejam opcionais para atualização
class PokemonUpdate(PokemonBase):
    name: str | None = None
    type: str | None = None
    level: int | None = None