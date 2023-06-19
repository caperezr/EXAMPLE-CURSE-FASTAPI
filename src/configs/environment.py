from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    DEBUG: bool = os.environ.get("DEBUG", False)
    ENV: str = os.environ.get("ENV", "dev")

    PROJECT_NAME: str = os.environ.get("PROJECT_NAME", "inventory-service")
    PROJECT_API_VERSION: str = os.environ.get("PROJECT_API_VERSION", "0.1.0")
    DOCS_URL: str = os.environ.get("DOCS_URL", None)
    REDOC_URL: str = os.environ.get("REDOC_URL", None)
