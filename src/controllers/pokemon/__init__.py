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

        print("nombre de pokemon requeste: ", name_pokemon)

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

    @staticmethod
    async def get_byid_pokemon_filter(id: int):
        print("ID de Pokemon solicitado:", id)

        url = f"https://pokeapi.co/api/v2/pokemon/{id}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            id = data["id"]
            name = data["name"]
            forms = data["forms"]
            url = forms[0]["url"]
            # Filtrar para el url de la imagen
            sprites = data["sprites"]
            other = sprites["other"]
            dream_world = other["dream_world"]
            imgUrl = dream_world["front_default"]

            pokemon_data = PokemonResponse(id=id, name=name, url=url, imgUrl=imgUrl)
            return pokemon_data
        else:
            return None
