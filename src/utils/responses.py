from starlette.responses import JSONResponse

# from fastapi import status


class ResponseJson(JSONResponse):
    def __init__(self, content, *args, **kwargs):
        # status_code = kwargs.get("status_code", 200)
        # message = kwargs.get('message', "Consulta exitosa")
        # response = {
        #   'status_code': status_code,
        #   'message': message,
        # }

        # if not content is None:
        #   response['data'] = content

        super().__init__(
            content=content,
            media_type="application/json",
            *args,
            **kwargs,
        )
