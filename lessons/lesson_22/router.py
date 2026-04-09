from typing import Annotated
from fastapi import APIRouter, Body , Path
from pydantic import BaseModel

router = APIRouter(
    prefix="/lesson-22",
    tags=["Lesson 22"]
)

class Item(BaseModel):
    name : str
    description : str | None = None
    price : float 
    tax : float | None = None

@router.post(
    "/items/{item_id}",
    summary="Create an Item",
    description="Observe Body with Multiple Examples in the OpenAPI docs"
)
async def udpate_item(
    item_id: Annotated[int, Path(gt=0, le=100, description="The ID of the item to update")],
    item: Annotated[
        Item,
        Body(
            example=[
                {
                    "name": "Item 1",
                    "description": "This is item 1",
                    "price": 10.5,
                    "tax": 0.5
                },
                {
                    "name": "Item 2",
                    "description": "This is item 1",
                    "price": 10.5,
                    "tax": 0.5
                },
                ],)
        ]
):
    results = {"item_id": item_id, "item":item}
    return results
    