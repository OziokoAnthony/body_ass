from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register")
def register_user(username: str, email: str, password: str):
    if len(username) < 3:
        raise HTTPException(
            status_code=400,
            detail="Username must be at least 3 characters"
        )

    if "@" not in email or "." not in email:
        raise HTTPException(
            status_code=400,
            detail="Please enter a valid email"
        )

    if len(password) < 8:
        raise HTTPException(
            status_code=400,
            detail="Password must be at least 8 characters"
        )

    if not any(char.isupper() for char in password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain an uppercase letter"
        )

    if not any(char.isdigit() for char in password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain a number"
        )

    return {
        "message": "User registered successfully",
        "username": username,
        "email": email
    }
