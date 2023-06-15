from fastapi import Depends
from starlette.endpoints import HTTPEndpoint
import requests
from validators.ability.response import AbilityResponse
from utils.ability.pokemon import Pokemon


class AbilityResource(HTTPEndpoint):
    @staticmethod
    async def get_pokemon_by_ability(id: int):
        url = f"https://pokeapi.co/api/v2/ability/{id}"
        response = requests.get(url)
        data = response.json()

        name_ability = data["name"]

        listpokemonbyalility = []

        for pokemon in data["pokemon"]:
            pokemon_name = pokemon["pokemon"]["name"]

            pokemon_url = pokemon["pokemon"]["url"]

            pokemon_data = Pokemon(name=pokemon_name, url=pokemon_url)
            listpokemonbyalility.append(pokemon_data)

        pokemonsbyability = AbilityResponse(
            name=name_ability, pokemon=listpokemonbyalility
        )

        return pokemonsbyability
