from fastapi import FastAPI
from src.pets.routers import router as router_pet


app = FastAPI(
    title="Accounting for pets"
)

app.include_router(router_pet)
