from typing import Annotated
from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/lesson-7",
    tags=["Lesson 7"]
)

@router.get(
    "/items/",
    summary="Multiple query params with validation",
    description="Demonstrates query metadata addition using title, alias, and max_length using Query class."
)
async def read_items(q: Annotated[list[str] | None, Query(title= "Observationbs on car", max_length=20, alias="car-damage")] = None): # just list use is possible, no str
    results = {"items": [{"car_number": "HR01X"}, {"service_need": "Oil Change, Tire Rotation"}]}
    if q:
        results.update({"observations": q})
    return results