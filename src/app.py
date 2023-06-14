import sys

sys.path.append("./src")

from fastapi import FastAPI, HTTPException, Depends


## Routes
from routes import router as root


# Health check
@root.get("/health-check", tags=["Check"])
def health_check(_authorization=Depends(APIKeyHeader(name="Authorization"))):
    """Root"""
    return {
        "status": "OK",
        "version": getattr(Config, "PROJECT_API_VERSION", "0.1.0"),
        "env": getattr(Config, "ENV", "null"),
    }


# Adding routers
app.include_router(root)
