import time
from typing import Callable
from fastapi import Request, Response
from fastapi.routing import APIRoute
from configs.environment import Config
from exceptions.fast_api_custom import CustomException
from database.session import SessionLocal
from services.logging import logger
from jose import jwt


class AuthDbMiddleware(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(
            request: Request,
        ) -> Response:  # pylint: disable=too-many-branches
            try:
                logger.info(f"headers: {request.headers}")
                request_authorization = request.headers.get("Authorization", None)
                if not request_authorization:
                    raise CustomException(
                        status_code=412,
                        detail="Authorization headers are required.",
                        type="headers",
                        code=995,
                    )
                access_token_key = request_authorization.split(" ")[0]
                logger.info(f"primer elemento: , {access_token_key}")
                access_token_jwt = request_authorization.split(" ")[1]

                print("token prefijo: ", access_token_key)
                print("token key: ", access_token_jwt)
                print("env: ", Config.JWT_HASH_KEY)

                if access_token_key != Config.AWS_JWT_PREFIX:
                    raise CustomException(
                        status_code=401,
                        type="indetifier",
                        detail="El identificador del JWT es invalido!",
                    )

                toke_decode = jwt.decode(
                    access_token_jwt, Config.JWT_HASH_KEY, algorithms=["HS256"]
                )

                if toke_decode.get("service", "") != "pokemon":
                    raise CustomException(
                        status_code=401,
                        type="indetifier",
                        detail="El identificador del JWT es invalido!",
                    )

                # request.state.authorization = request_authorization
                # request.state.organization_id = request.headers.get(
                #    "organizationId", None
                # )

                ## Session DB
                request.state.db = SessionLocal()
                ## Time Response
                request.state.db.begin()
                before = time.time()
                response: Response = await original_route_handler(request)
                duration = time.time() - before
                response.headers["X-Response-Time"] = str(duration)
                # response.token= 'TOKENasasa'
                request.state.db.commit()
                return response
            except CustomException as err:
                logger.error(err)
                if hasattr(request.state, "db"):
                    request.state.db.rollback()
                raise CustomException(
                    status_code=err.status_code,
                    detail=err.detail,
                    type=err.type,
                    code=err.code,
                ) from err
            except Exception as err:
                logger.error(err)
                if hasattr(request.state, "db"):
                    request.state.db.rollback()
                raise CustomException(
                    status_code=500,
                    detail="We have some inconveniencies, please try it later.",
                ) from err
            finally:
                if hasattr(request.state, "db"):
                    request.state.db.close()

        return custom_route_handler
