import sys

sys.path.append("./src")

from fastapi import FastAPI, HTTPException, Depends
from routes import router as root
from configs.environment import Config
from utils.responses import ResponseJson

# FastAPI parameters
app = FastAPI(
    title=Config.PROJECT_NAME,
    version=Config.PROJECT_API_VERSION,
    debug=Config.DEBUG,
    # default_response_class=ResponseJson,
    docs_url=Config.DOCS_URL,
    redoc_url=Config.REDOC_URL,
)


""" @app.on_event("startup")
async def startup():
    print(Config.DOCS_URL),
    print(Config.DB_HOST)
    create_tables() """


app.include_router(root)
