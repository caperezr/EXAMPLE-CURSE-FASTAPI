from fastapi import APIRouter

router = APIRouter()

@router.get("/all")
def get_electricidad():
    return {"message": "Información sobre electricidad"}