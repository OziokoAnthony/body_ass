from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_user_registration():
    response = client.post(
        "/users/register",
        params={
            "username": "anthony",
            "email": "anthony@example.com",
            "password": "Password123"
        }
    )
    assert response.status_code == 200


def test_product_search():
    response = client.get(
        "/products/search",
        params={"category": "electronics"}
    )
    assert response.status_code == 200


def test_vehicle():
    response = client.get("/vehicles/1")
    assert response.status_code == 200


def test_flight_booking():
    response = client.post(
        "/flights/book",
        params={
            "passenger_name": "John Doe",
            "age": 25,
            "contact": "08012345678",
            "origin": "Lagos",
            "destination": "Abuja",
            "flight_date": "2030-05-10",
            "seat_preference": "window"
        }
    )
    assert response.status_code == 200


def test_event_booking():
    response = client.post(
        "/events/book",
        params={
            "attendee_name": "John Doe",
            "email": "john@example.com",
            "age": 25,
            "event_name": "Python Workshop",
            "event_date": "2030-05-10",
            "location": "Enugu",
            "ticket_type": "regular"
        }
    )
    assert response.status_code == 200
