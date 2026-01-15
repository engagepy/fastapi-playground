from typing import Annotated
from fastapi import APIRouter, Query
from pydantic import AfterValidator

router = APIRouter(
    prefix="/lesson-8",
    tags=["Lesson 8"]
)


damage_type_prefixes = {
    "dent",
    "scratch",
    "broken glass",
    "paint chip",
    "bumper damage",
    "wheel damage",
    "roof damage",
    "mirror damage",
    "headlight damage",
    "tail light damage",
    "door damage",
    "hood damage",
    "trunk damage",
    "frame damage",
    "undercarriage damage",
    "exhaust damage",
    "suspension damage",
    "interior damage",
    "electrical damage",
}

def check_prefix(value: list[str]) -> list[str]:
    for item in value:
        if not any(item.startswith(prefix) for prefix in damage_type_prefixes):
            raise ValueError(f"Each observation must start with a valid damage type prefix: {', '.join(damage_type_prefixes)}")
    return value

@router.get(
    "/items/",
    summary="Multiple query params with validation",
    description="Demonstrates query or path parameter validation using AfterValidator from Pydantic."
)
async def read_items(
    q: Annotated[list[str] | None, 
        
        Query(
            title= "Observationbs on car", 
            max_length=20, 
            alias="car-damage"),
            AfterValidator(check_prefix)] = None
            ): # just list use is possible, no str
    results = {"items": [{"car_number": "HR01X"}, {"service_need": "Oil Change, Tire Rotation"}]}
    if q:
        results.update({"observations": q})
    return results