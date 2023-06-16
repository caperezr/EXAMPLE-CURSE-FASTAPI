from fastapi import APIRouter
from controllers.exercise import ExerciseResource

router = APIRouter(prefix="/exercise")

router.add_api_route(
    "/items",
    ExerciseResource.get_params,
    methods=["GET"],
    tags=["exercise"],
    name="Get params from url",
    response_model=str,
)
