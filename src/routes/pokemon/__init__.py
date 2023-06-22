from fastapi import APIRouter
from controllers.pokemon import PokemonResource
from validators.pokemon.response import PokemonResponse, ResponseTemplete
from typing import Optional

router = APIRouter(prefix="/pokemon")

# Routes for the API
router.add_api_route(
    "/all",
    PokemonResource.get_all_pokemon_filter,
    methods=["GET"],
    tags=["pokemon"],
    name="Get all pokemon",
    response_model=list[ResponseTemplete],
)

router.add_api_route(
    "/byname",
    PokemonResource.get_byname_pokemon_filter,
    methods=["POST"],
    tags=["pokemon"],
    name="Get pokemon by name",
    response_model=Optional[ResponseTemplete],
)

router.add_api_route(
    "/byid/{id}",
    PokemonResource.get_byid_pokemon_filter,
    methods=["GET"],
    tags=["pokemon"],
    name="Get pokemon by id",
    response_model=Optional[PokemonResponse],
)
