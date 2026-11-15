import httpx


#Receber o nome de um Pokémon como argumento
def get_pokemon(name: str):
    try:
        #Fazer uma requisição GET para a API do PokeAPI Para fazer uma requisição, usamos httpx.get().
        response = httpx.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")
        response.raise_for_status()  # Levanta um erro se a resposta não for bem-sucedida
        data = response.json()
        return {
            "id": data["id"],
            "name": data["name"],
            "type": [t["type"]["name"] for t in data["types"]],
            "base_experience": data["base_experience"],
            "height": data["height"],
            "weight": data["weight"],
            "sprites": data["sprites"]["front_default"]
        }
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return {"error": "Pokémon não encontrado."}
        else:
            return {"error": "Ocorreu um erro ao buscar o Pokémon."}    
    except httpx.RequestError as e:
        return {"error": "Não foi possível conectar à PokéAPI."}