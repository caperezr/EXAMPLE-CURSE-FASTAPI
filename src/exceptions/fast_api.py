from fastapi import Request
from fastapi.responses import JSONResponse
from exceptions.fast_status_error import error_custom


# Aqui entra error de FastApi y SqlAlchemy
async def http_exception_handler(request: Request, exception):
    try:
        status_code = exception.status_code
    except Exception:
        status_code = 500

    try:
        detail = exception.detail
    except Exception:
        if error_custom.get(status_code):
            detail = error_custom[status_code]["detail"]
        else:
            detail = "We're presenting some problems with the server. Please try again later."

    return JSONResponse(
        status_code=status_code,
        content={
            "error": {
                "message": detail,
                "code": 1546,
            },
            "type": "ServerApi",
            "status_code": status_code,
        },
    )


async def http_exception_handler_custom(request: Request, exception):
    detail = exception.detail
    status_code = exception.status_code
    type = exception.type
    code = exception.code

    return JSONResponse(
        status_code=status_code,
        content={
            "error": {
                "message": detail,
                "code": code,
            },
            "type": type,
            "status_code": status_code,
        },
    )


async def validation_exception_handler(request: Request, exception):
    try:
        errors = exception.errors()
    except Exception as ex:
        errors = exception.manual

    try:
        errors_finals = []
        fields_error = {}

        for value in list(errors):
            print("error", value)
            types = value["type"].split(".")
            type_value = types[1]
            msg = value["msg"]
            fields = list(value["loc"])[1]

            if type_value == "jsondecode":
                return JSONResponse(
                    status_code=500,
                    content={
                        "error": {},
                        "message": "Incorrect JSON validation",
                        "type": "ValidateFields",
                        "code": 189,
                        "status_code": 500,
                    },
                )
            elif type_value == "email":
                fields_error.update({fields: "Incorrect email"})
            elif type_value == "uuid":
                fields_error.update({fields: "Value is not a valid UUID"})
            elif type_value == "integer":
                fields_error.update({fields: "Value is not a valid integer"})
            elif type_value == "float":
                fields_error.update({fields: "Value is not a valid float"})
            elif type_value == "bool":
                fields_error.update({fields: "Value is not a valid boolean"})
            elif type_value == "json":
                fields_error.update({fields: "Invalid JSON"})
            elif type_value == "none":
                fields_error.update({fields: "Field needs have a value"})
            elif type_value == "missing":
                fields_error.update({fields: "Value is required"})
            elif type_value == "any_str":
                character_max = [int(s) for s in msg.split() if s.isdigit()][0]
                if types[2] == "min_length":
                    fields_error.update(
                        {
                            fields: f"Make sure this value has at least {character_max} characters"
                        }
                    )
                elif types[2] == "max_length":
                    fields_error.update(
                        {
                            fields: f"Make sure this value has at most {character_max} characters"
                        }
                    )
                else:
                    fields_error.update(
                        {fields: f"Make sure that this value has allowed characters"}
                    )
            else:
                errors_finals.append(
                    {"type": type_value, "detail": msg, "field": fields}
                )

        return JSONResponse(
            status_code=422,
            content={
                "errors": fields_error,
                "message": "Incorrect validation of parameters",
                "type": "ValidateFields",
                "code": 190,
                "status_code": 422,
            },
        )

    except Exception as ex:
        return JSONResponse(
            status_code=422,
            content={
                "error": {
                    "message": "Validation of fields failed",
                    "type": "ValidateFields",
                    "code": 191,
                },
                "status_code": 422,
            },
        )
