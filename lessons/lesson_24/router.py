from typing import Annotated
from fastapi import APIRouter, Cookie
from pydantic import BaseModel

router = APIRouter(
    prefix="/lesson-24",
    tags=["Lesson 24"]
)

@router.get(
    "/items", 
    summary="Use fastapi built in Cookie parameters", 
    description="Observe how to use cookie parameters in the OpenAPI docs"
    )
async def read_items(ads_id: Annotated[str, Cookie()] = None):
    return {"ads_id": ads_id}

