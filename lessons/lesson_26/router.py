from typing import Annotated
from fastapi import APIRouter, Cookie
from pydantic import BaseModel


router = APIRouter( 
    prefix="/lesson-26", 
    tags=["Lesson 26"]
)

class Cookies(BaseModel):
    ads_id: str | None = None
    fatebook: str | None = None
    googla: str | None = None


@router.get(
    "/items",
    summary="Get items with Cookie parameters",
    description="Observe how to use Cookie parameters in the OpenAPI docs"
)
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies.dict()

