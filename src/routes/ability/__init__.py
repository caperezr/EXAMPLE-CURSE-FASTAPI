from fastapi import APIRouter
from controllers.ability import AbilityResource
from validators.ability.response import AbilityResponse
from typing import Optional

router = APIRouter(prefix="/ability")

# Routes for the API
router.add_api_route(
    "/byid/{id}",
    AbilityResource.get_pokemon_by_ability,
    methods=["GET"],
    tags=["ability"],
    name="Get all pokemon by ability id",
    response_model=Optional[AbilityResponse],
)
