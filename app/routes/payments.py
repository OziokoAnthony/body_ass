from datetime import datetime
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/payments", tags=["Payments"])


@router.post("/process")
def process_payment(
    amount: float,
    card_number: str,
    expiration_date: str,
    cvv: str
):
    if amount <= 0:
        raise HTTPException(
            status_code=400,
            detail="Payment amount must be greater than 0"
        )

    if not card_number.isdigit() or len(card_number) != 16:
        raise HTTPException(
            status_code=400,
            detail="Card number must contain 16 digits"
        )

    if not cvv.isdigit() or len(cvv) != 3:
        raise HTTPException(
            status_code=400,
            detail="CVV must contain 3 digits"
        )

    try:
        expiry = datetime.strptime(expiration_date, "%m/%Y")
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Expiration date must use MM/YYYY format"
        )

    current_month = datetime.now().replace(day=1)

    if expiry < current_month:
        raise HTTPException(
            status_code=400,
            detail="Card has expired"
        )

    # This is only a classroom simulation.
    return {
        "message": "Payment processed successfully",
        "amount": amount,
        "status": "successful"
    }
