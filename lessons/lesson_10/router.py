from typing import Annotated
from pydantic import AfterValidator
from fastapi import APIRouter, Query, Path
import enum
import random


router = APIRouter(
    prefix="/lesson-10",
    tags=["Lesson 10"])

@router.post("/cart/{user_id}/item/{item_id}")
async def cart_items(
    user_id: Annotated[str, Path(title="Alphanumeric User ID", min_length=5, max_length=15)],
    item_id: Annotated[int, Path(title="Item ID", ge=1)],
):
    return {"user_id": user_id, "item_id": item_id}