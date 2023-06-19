from fastapi import Depends
from starlette.endpoints import HTTPEndpoint


class ExerciseResource(HTTPEndpoint):
    @staticmethod
    async def get_params(params: dict):
        for key, value in params.items():
            print(f"Key: {key}, Value: {value}")
        return "Parametros recibidos 123"
    
    @staticmethod
    async def get_field(request):
        argument1 = request.args.get("argument1")
        argument2 = request.args.get("argument2")
        print("argumento 1: ", argument1)
        print("argumento 2: ", argument2)
        return False
