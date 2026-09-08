from datetime import date
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/events", tags=["Events"])


@router.post("/book")
def book_event(
    attendee_name: str,
    email: str,
    age: int,
    event_name: str,
    event_date: date,
    location: str,
    ticket_type: str
):
    if len(attendee_name) < 2:
        raise HTTPException(
            status_code=400,
            detail="Attendee name is too short"
        )

    if "@" not in email or "." not in email:
        raise HTTPException(
            status_code=400,
            detail="Please enter a valid email"
        )

    if age < 1 or age > 120:
        raise HTTPException(
            status_code=400,
            detail="Age must be between 1 and 120"
        )

    if len(event_name) < 2:
        raise HTTPException(
            status_code=400,
            detail="Event name is too short"
        )

    if len(location) < 2:
        raise HTTPException(
            status_code=400,
            detail="Location is required"
        )

    valid_tickets = ["regular", "vip", "student"]

    if ticket_type.lower() not in valid_tickets:
        raise HTTPException(
            status_code=400,
            detail="Ticket type must be regular, vip, or student"
        )

    if event_date < date.today():
        raise HTTPException(
            status_code=400,
            detail="Event date cannot be in the past"
        )

    return {
        "message": "Event booking successful",
        "attendee": attendee_name,
        "email": email,
        "event": event_name,
        "date": str(event_date),
        "location": location,
        "ticket_type": ticket_type.lower(),
        "status": "confirmed"
    }
