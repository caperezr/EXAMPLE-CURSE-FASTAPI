from fastapi import Depends
from starlette.endpoints import HTTPEndpoint
import requests
from validators.ability.response import AbilityResponse, TemplateResponseById
from validators.ability.request import AbilityRequest
from utils.ability.pokemon import Pokemon


class AbilityResource(HTTPEndpoint):
    @staticmethod
    async def get_all_ability():
        url = "https://pokeapi.co/api/v2/ability/"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            results = data["results"]

            ability_list = []
            for result in results:
                name = result["name"]
                url = result["url"]
                ability_data = AbilityResponse(name=name, url=url)
                ability_list.append(ability_data)
            return ability_list
        else:
            return None

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
        pokemonsbyability = TemplateResponseById(
            name=name_ability, pokemon=listpokemonbyalility
        )
        return pokemonsbyability

    @staticmethod
    async def get_pokemon_by_ability_name(datas: AbilityRequest):
        name_ability = datas.name
        url = f"https://pokeapi.co/api/v2/ability/{name_ability}"
        response = requests.get(url)
        listpokemonbyalility = []
        if response.status_code == 200:
            data = response.json()
            for pokemon in data["pokemon"]:
                pokemon_name = pokemon["pokemon"]["name"]
                pokemon_url = pokemon["pokemon"]["url"]
                pokemon_data = Pokemon(name=pokemon_name, url=pokemon_url)
                listpokemonbyalility.append(pokemon_data)
            pokemonsbyability = TemplateResponseById(
                name=name_ability, pokemon=listpokemonbyalility
            )
            return pokemonsbyability
        else:
            return None
