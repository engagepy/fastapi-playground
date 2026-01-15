from typing import Annotated
from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/lesson-7",
    tags=["Lesson 7"]
)

@router.get(
    "/items/",
    summary="Multiple query params with validation",
    description="Demonstrates multiple query parameters with uniform validation using FastAPI Query."
)
async def read_items(q: Annotated[list[str] | None, Query(max_length=20)] = None): # just list use is possible, no str
    results = {"items": [{"car_number": "HR01X"}, {"service_need": "Oil Change, Tire Rotation"}]}
    if q:
        results.update({"observations": q})
    return results