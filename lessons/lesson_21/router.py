from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl
from typing import Annotated

router = APIRouter(
    prefix="/lesson-21",
    tags=["Lesson 21"]
)

class grocery_basket(BaseModel):
    items: list[str]
    total_price: float
    store_url: HttpUrl

    model_config = {
        "schema_extra": {
            "example": {
                "items": ["milk", "bread", "eggs"],
                "total_price": 12.50,
                "store_url": "https://www.example.com/store"
            }
        }
    }

@router.post(
    "/grocery-basket",
    summary="Create a Grocery Basket",
    description="Endpoint to create a grocery basket with items, total price, and store URL."
)

async def create_grocery_basket(basket: grocery_basket):
    return {"message": "Grocery basket created successfully!", "basket": basket}


