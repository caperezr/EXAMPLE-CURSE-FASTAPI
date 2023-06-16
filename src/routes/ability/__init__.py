from fastapi import APIRouter
from controllers.ability import AbilityResource
from validators.ability.response import AbilityResponse
from typing import Optional

router = APIRouter(prefix="/ability")

# Routes for the API
router.add_api_route(
    "/all",
    AbilityResource.get_all_ability,
    methods=["GET"],
    tags=["ability"],
    name="Get all abilities",
    response_model=list[AbilityResponse],
)

router.add_api_route(
    "/byid/{id}",
    AbilityResource.get_pokemon_by_ability,
    methods=["GET"],
    tags=["ability"],
    name="Get all pokemon by ability id",
    response_model=Optional[AbilityResponse],
)

router.add_api_route(
    "/byname",
    AbilityResource.get_pokemon_by_ability_name,
    methods=["POST"],
    tags=["ability"],
    name="Get all pokemon by ability name",
    response_model=Optional[AbilityResponse],
)
