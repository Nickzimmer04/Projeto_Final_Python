from pydantic import BaseModel, Field

class PokemonBase(BaseModel):
    name: str = Field(description="Nome do Pokémon")
    type: str = Field(description="Tipo do Pokémon")
    level: int = Field(description="Nível do Pokémon")


class PokemonUpdate(BaseModel):
    name: str | None = Field(default=None, description="Nome do Pokémon")
    type: str | None = Field(default=None, description="Tipo do Pokémon")
    level: int | None = Field(default=None, description="Nível do Pokémon")