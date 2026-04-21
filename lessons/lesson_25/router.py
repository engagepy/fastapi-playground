from fastapi import APIRouter, Header
from pydantic import BaseModel
from typing import Annotated


router = APIRouter(
    prefix="/lesson-25",
    tags=["Lesson 25"]
)

@router.get(
    "/items",
    summary="Get items with Header parameters",
    description="Observe how to use Header parameters in the OpenAPI docs"
)
async def read_items(user_agent: Annotated[str, Header()] = None):
    return {"User-Agent": user_agent}