from fastapi import APIRouter, Path, Query, HTTPException

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])


vehicles = [
    {"id": 1, "make": "Toyota", "model": "Camry", "price": 12000000},
    {"id": 2, "make": "Honda", "model": "Civic", "price": 10000000},
    {"id": 3, "make": "Toyota", "model": "Corolla", "price": 9000000},
]


@router.get("/")
def get_vehicles(
    make: str | None = Query(default=None, min_length=2),
    model: str | None = Query(default=None, min_length=2),
    min_price: float | None = Query(default=None, ge=0),
    max_price: float | None = Query(default=None, ge=0)
):
    result = []

    for vehicle in vehicles:
        if make is not None and make.lower() != vehicle["make"].lower():
            continue

        if model is not None and model.lower() != vehicle["model"].lower():
            continue

        if min_price is not None and vehicle["price"] < min_price:
            continue

        if max_price is not None and vehicle["price"] > max_price:
            continue

        result.append(vehicle)

    return result


@router.get("/{vehicle_id}")
def get_vehicle(
    vehicle_id: int = Path(..., ge=1)
):
    for vehicle in vehicles:
        if vehicle["id"] == vehicle_id:
            return vehicle

    raise HTTPException(
        status_code=404,
        detail="Vehicle not found"
    )
