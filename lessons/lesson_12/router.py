from typing import Annotated, Literal
from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel, Field
import enum
import random

router = APIRouter(
    prefix="/lesson-12",
    tags=["Lesson 12"]
)

class Basket(BaseModel):
    id: int
    items: list[str] = Field(..., description="List of items in the basket")
    total_price: float = Field(..., description="Total price of the basket")


@router.put("/baskets/{basket_id}", response_model=Basket)
async def get_basket(
    basket_id: Annotated[int, Path(gt=0,le=100, description="The ID of the basket to retrieve")],
    q : str | None = Query(default=None, max_length=50, description="Optional query string to filter results"),
    basket: Basket | None = None
):
    result = {"id" : basket_id}
    if q:
        result.update({"query": q})
    if basket:
        result.update({"basket": basket})
    return result


    
