from fastapi import FastAPI
from routes import router as routes_router
from database import create_tables

app = FastAPI()


@app.on_event("startup")
async def startup():
    create_tables()


app.include_router(routes_router)
