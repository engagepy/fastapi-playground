from enum import Enum
from datetime import datetime

from fastapi import APIRouter

router = APIRouter(
    prefix="/lesson-1",
    tags=["Lesson 1"]
)

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@router.get(
    "/models/{model_name}",
    summary="Enum path parameter and conditional logic",
    description="Demonstrates Enum usage as a path parameter and conditional branching based on the value."
)
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Getting the hands on AlexNet"}
    if model_name == ModelName.resnet:
        return {"model_name": model_name, "message": "Getting the ResNet model"}
    return {"model_name": model_name, "message": "Getting the LeNet model"}

@router.get(
    "/age/{age}",
    summary="Query parameters with defaults and optionals",
    description="Demonstrates query parameters, default values, optional parameters, and a boolean toggle."
)
async def calculate_age(
    age: int,
    desired_age: int,
    activate: bool = True
):
    years_needed = desired_age - age
    current_year = datetime.now().year
    future_year = current_year + years_needed if activate else current_year    

    return {"current_year": current_year, "future_age": desired_age, "year": future_year}