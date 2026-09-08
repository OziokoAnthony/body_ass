from fastapi import APIRouter, Query

router = APIRouter(prefix="/products", tags=["Products"])


products = [
    {"name": "Laptop", "category": "electronics", "price": 500000},
    {"name": "Phone", "category": "electronics", "price": 250000},
    {"name": "School Bag", "category": "school", "price": 25000},
    {"name": "Shoes", "category": "fashion", "price": 50000},
]


@router.get("/search")
def search_products(
    name: str | None = Query(default=None, min_length=2),
    category: str | None = Query(default=None, min_length=2),
    min_price: float | None = Query(default=None, ge=0),
    max_price: float | None = Query(default=None, ge=0)
):
    if min_price is not None and max_price is not None:
        if min_price > max_price:
            return {"message": "min_price cannot be greater than max_price"}

    result = []

    for product in products:
        if name is not None:
            if name.lower() not in product["name"].lower():
                continue

        if category is not None:
            if category.lower() != product["category"].lower():
                continue

        if min_price is not None:
            if product["price"] < min_price:
                continue

        if max_price is not None:
            if product["price"] > max_price:
                continue

        result.append(product)

    return {
        "count": len(result),
        "products": result
    }
