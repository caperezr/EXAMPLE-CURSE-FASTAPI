from fastapi import APIRouter

router = APIRouter()

@router.get("/all")
def get_electricidad():
    return {"message": "Información sobre pokemones de electricidad"}

@router.get("/byname/{pokemon_name}")
def get_pokemon_electricity_by_name(pokemon_name: str):
    return {"message": f"Información sobre el pokemon de electricidad llamado : {pokemon_name}"}