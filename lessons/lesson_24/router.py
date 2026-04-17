from typing import Annotated
from fastapi import APIRouter, Cookie
from pydantic import BaseModel

router = APIRouter(
    prefix="/lesson-24",
    tags=["Lesson 24"]
)

@router.get(
    "/items", 
    summary="Get items with query parameters", 
    description="Observe how to use query parameters in the OpenAPI docs"
    )
async def read_items(ads_id: Annotated[str, Cookie()] = None):
    return {"ads_id": ads_id}

