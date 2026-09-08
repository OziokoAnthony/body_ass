from datetime import date
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/flights", tags=["Flights"])


@router.post("/book")
def book_flight(
    passenger_name: str,
    age: int,
    contact: str,
    origin: str,
    destination: str,
    flight_date: date,
    seat_preference: str
):
    if len(passenger_name) < 2:
        raise HTTPException(
            status_code=400,
            detail="Passenger name is too short"
        )

    if age < 1 or age > 120:
        raise HTTPException(
            status_code=400,
            detail="Passenger age must be between 1 and 120"
        )

    if len(contact) < 7:
        raise HTTPException(
            status_code=400,
            detail="Contact details are invalid"
        )

    if len(origin) < 2 or len(destination) < 2:
        raise HTTPException(
            status_code=400,
            detail="Origin and destination are required"
        )

    valid_seats = ["window", "middle", "aisle"]

    if seat_preference.lower() not in valid_seats:
        raise HTTPException(
            status_code=400,
            detail="Seat must be window, middle, or aisle"
        )

    if flight_date < date.today():
        raise HTTPException(
            status_code=400,
            detail="Flight date cannot be in the past"
        )

    return {
        "message": "Flight booked successfully",
        "passenger": passenger_name,
        "origin": origin,
        "destination": destination,
        "flight_date": str(flight_date),
        "seat": seat_preference.lower(),
        "status": "confirmed"
    }
