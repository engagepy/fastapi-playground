from typing import Annotated, Literal
from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel, Field
import enum
import random

router = APIRouter(
    prefix="/lesson-12",
    tags=["Lesson 12"]
)


section = enum.Enum(
    "section",
    {
        "fruits": 1,
        "vegetables": 2,
        "dairy": 3,
        "bakery": 4
    }
)

class Basket(BaseModel):
    item_zone: section = Field(..., description="Section of the basket")
    items: list[str] = Field(..., description="List of items in the basket")
    total_price: float = Field(..., description="Total price of the basket")


@router.put(
        "/baskets/{basket_id}",
        summary="Mix Path, Query, and Body parameter with 'Path','Query validation",
        description="Demonstrates path, query, and body parameter validation using Pydantic models"
        )
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


    
