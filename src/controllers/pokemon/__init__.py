from fastapi import Depends
from starlette.endpoints import HTTPEndpoint
from validators.pokemon.response import PokemonResponse
from validators.pokemon.request import PokemonRequest
import requests


class PokemonResource(HTTPEndpoint):
    @staticmethod
    async def get_all_pokemon_filter():
        url = "https://pokeapi.co/api/v2/pokemon/"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            results = data["results"]

            pokemon_list = []
            for result in results:
                name = result["name"]
                url = result["url"]
                pokemon_data = PokemonResponse(name=name, url=url)
                pokemon_list.append(pokemon_data)

            return pokemon_list
        else:
            return None

    @staticmethod
    async def get_byname_pokemon_filter(datas: PokemonRequest):
        name_pokemon = datas.name
        # return name_pokemon

        url = "https://pokeapi.co/api/v2/pokemon/"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            results = data["results"]

            for result in results:
                name = result["name"]
                url = result["url"]
                pokemon_data = PokemonResponse(name=name, url=url)
                print("nombre de pokemon requeste: ", name_pokemon)
                print("nombre de la lista: ", pokemon_data.name)
                if pokemon_data.name == name_pokemon:
                    return pokemon_data
                else:
                    return None
        else:
            return None
