
def test_list_pokemon(client):
    response = client.get("/pokemon")

    assert response.status_code == 200
    assert response.json() == []

def test_create_pokemon(client):
    response = client.post(
        "/pokemon",
        json={
            "name": "pikachu",
            "type": "electric",
            "level": 10
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["pokemon"]["name"] == "pikachu"
    assert data["pokemon"]["type"] == "electric"
    assert data["pokemon"]["level"] == 10

def test_create_and_list_pokemon(client):
    response = client.post(
        "/pokemon",
        json={
            "name": "bulbasaur",
            "type": "grass",
            "level": 5
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["pokemon"]["name"] == "bulbasaur"
    assert data["pokemon"]["type"] == "grass"
    assert data["pokemon"]["level"] == 5


    response = client.get("/pokemon")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "bulbasaur"

def test_create_duplicate_pokemon(client):
    response = client.post(
        "/pokemon",
        json={
            "name": "bulbasaur",
            "type": "grass",
            "level": 5
        }
    )
    assert response.status_code == 200

    response = client.post(
        "/pokemon",
        json={
            "name": "bulbasaur",
            "type": "grass",
            "level": 5
        }
    )

    assert response.status_code == 409
    assert response.json()["detail"] == "Pokémon com o nome 'bulbasaur' já existe."

def test_get_pokemon_by_id(client):
    # Cadastrar um Pokémon
    response = client.post(
        "/pokemon",
        json={
            "name": "charmander",
            "type": "fire",
            "level": 10
        }
    )

    assert response.status_code == 200

    # Buscar o Pokémon pelo ID
    pokemon_id = response.json()["pokemon"]["id"]

    response = client.get(f"/pokemon/id/{pokemon_id}")

    assert response.status_code == 200
    assert response.json()["name"] == "charmander"
    assert response.json()["type"] == "fire"
    assert response.json()["level"] == 10

def test_get_pokemon_by_id_not_found(client):
    response = client.get("/pokemon/id/9999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Pokémon não encontrado"

def test_update_pokemon(client):
    response = client.post(
        "/pokemon",
        json={
            "name": "squirtle",
            "type": "water",
            "level": 5
        }
    )

    assert response.status_code == 200

    pokemon_id = response.json()["pokemon"]["id"]

    response = client.put(
        f"/pokemon/{pokemon_id}",
        json={
            "level": 15
        }
    )

    assert response.status_code == 200

    response = client.get(f"/pokemon/id/{pokemon_id}")

    assert response.status_code == 200
    assert response.json()["level"] == 15

def test_delete_pokemon(client):
    response = client.post(
        "/pokemon",
        json={
            "name": "eevee",
            "type": "normal",
            "level": 10
        }
    )

    assert response.status_code == 200

    pokemon_id = response.json()["pokemon"]["id"]

    # Excluir o Pokémon
    response = client.delete(f"/pokemon/{pokemon_id}")

    assert response.status_code == 200

    # Verificar se ele realmente foi excluído
    response = client.get(f"/pokemon/id/{pokemon_id}")

    assert response.status_code == 404
    assert response.json()["detail"] == "Pokémon não encontrado"

def test_update_pokemon_not_found(client):
    response = client.put(
        "/pokemon/9999",
        json={
            "level": 20
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Pokémon não encontrado"

def test_delete_pokemon_not_found(client):
    response = client.delete("/pokemon/9999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Pokémon não encontrado"

def test_list_pokemon_pagination(client):
    pokemons = [
        {"name": "pikachu", "type": "electric", "level": 10},
        {"name": "bulbasaur", "type": "grass", "level": 5},
        {"name": "charmander", "type": "fire", "level": 8}
    ]

    for pokemon in pokemons:
        response = client.post("/pokemon", json=pokemon)
        assert response.status_code == 200

    response = client.get("/pokemon?skip=0&limit=2")

    assert response.status_code == 200
    assert len(response.json()) == 2

    response = client.get("/pokemon?skip=2&limit=2")

    assert response.status_code == 200
    assert len(response.json()) == 1

def test_create_pokemon_invalid_level(client):
    response = client.post(
        "/pokemon",
        json={
            "name": "pikachu",
            "type": "electric",
            "level": "abc"
        }
    )

    assert response.status_code == 422

def test_create_pokemon_without_name(client):
    response = client.post(
        "/pokemon",
        json={
            "type": "electric",
            "level": 10
        }
    )

    assert response.status_code == 422

def test_update_pokemon_invalid_level(client):
    # Cadastrar um Pokémon
    response = client.post(
        "/pokemon",
        json={
            "name": "pikachu",
            "type": "electric",
            "level": 10
        }
    )

    assert response.status_code == 200

    pokemon_id = response.json()["pokemon"]["id"]

    # Tentar atualizar com nível inválido
    response = client.put(
        f"/pokemon/{pokemon_id}",
        json={
            "level": "abc"
        }
    )

    assert response.status_code == 422

def test_update_pokemon_duplicate_name(client):
    # Cadastrar Pikachu
    response = client.post(
        "/pokemon",
        json={
            "name": "pikachu",
            "type": "electric",
            "level": 10
        }
    )
    assert response.status_code == 200

    # Cadastrar Bulbasaur
    response = client.post(
        "/pokemon",
        json={
            "name": "bulbasaur",
            "type": "grass",
            "level": 5
        }
    )
    assert response.status_code == 200

    bulbasaur_id = response.json()["pokemon"]["id"]

    # Tentar alterar o nome do Bulbasaur para Pikachu
    response = client.put(
        f"/pokemon/{bulbasaur_id}",
        json={
            "name": "pikachu"
        }
    )

    assert response.status_code == 409