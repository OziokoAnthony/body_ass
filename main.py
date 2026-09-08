from fastapi import FastAPI

from app.routes import users
from app.routes import products
from app.routes import payments
from app.routes import vehicles
from app.routes import flights
from app.routes import events

app = FastAPI(title="FastAPI Body Assignment")

app.include_router(users.router)
app.include_router(products.router)
app.include_router(payments.router)
app.include_router(vehicles.router)
app.include_router(flights.router)
app.include_router(events.router)


@app.get("/")
def home():
    return {"message": "FastAPI assignment is running"}
