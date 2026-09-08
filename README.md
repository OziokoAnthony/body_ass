# FastAPI Body Assignment


## Important

You asked for the project without Pydantic schema/model files.

The request values are handled directly inside each route. FastAPI's
basic validation tools such as Query and Path are used where needed.

## Project structure

```text
fastapi_body_assignment/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   └── routes/
│       ├── __init__.py
│       ├── users.py
│       ├── products.py
│       ├── payments.py
│       ├── vehicles.py
│       ├── flights.py
│       └── events.py
│
├── tests/
│   ├── __init__.py
│   └── test_api.py
│
├── requirements.txt
└── README.md
```

## Install

Create and activate your virtual environment first.

Then run:

```bash
pip install -r requirements.txt
```

## Run the server

From the project root:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Run tests

```bash
pytest
```

## Endpoints

### 1. User Registration

```text
POST /users/register
```

Example parameters:

```text
username=anthony
email=anthony@example.com
password=Password123
```

### 2. Product Search

```text
GET /products/search
```

Examples:

```text
/products/search
/products/search?name=phone
/products/search?category=electronics
/products/search?min_price=10000&max_price=300000
```

### 3. Payment Processing

```text
POST /payments/process
```

This is only a classroom simulation. Do not use real card information.

### 4. Vehicle Inventory

Get all/filter vehicles:

```text
GET /vehicles/
```

Get one vehicle:

```text
GET /vehicles/1
```

### 5. Flight Booking

```text
POST /flights/book
```

Seat options:

```text
window
middle
aisle
```

### 6. Event Booking

```text
POST /events/book
```

Ticket options:

```text
regular
vip
student
```
