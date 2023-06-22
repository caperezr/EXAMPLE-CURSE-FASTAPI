import sys

sys.path.append("./src")

from fastapi import FastAPI, HTTPException, Depends
from routes import router as root
from configs.environment import Config
from fastapi.exceptions import RequestValidationError
from utils.responses import ResponseJson
from fastapi.middleware.cors import CORSMiddleware


## Exceptions
from exceptions.fast_api_validation import ValidationException
from exceptions.fast_api_custom import CustomException
from exceptions.fast_api import (
    http_exception_handler_custom,
    http_exception_handler,
    validation_exception_handler,
)


# FastAPI parameters
app = FastAPI(
    title=Config.PROJECT_NAME,
    version=Config.PROJECT_API_VERSION,
    debug=Config.DEBUG,
    # default_response_class=ResponseJson,
    docs_url=Config.DOCS_URL,
    redoc_url=Config.REDOC_URL,
)

# Authorizations
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    # allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception handlers
app.add_exception_handler(CustomException, http_exception_handler_custom)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(ValidationException, validation_exception_handler)


app.include_router(root)
