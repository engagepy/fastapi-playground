from fastapi import APIRouter, Body
from pydantic import BaseModel, HttpUrl
from typing import Annotated

router = APIRouter(
    prefix="/lesson-20",
    tags=["Lesson 20"]  
)

class ImageRequest(BaseModel):
    url: HttpUrl
    name: str

@router.post(
    "images/upload-multiple",
    summary="Upload Multiple Images Pur Lists []",
    description="Endpoint to upload multiple images at once."
    )
async def upload_multiple_images(images: list[ImageRequest]):
    return {"message": f"Received {len(images)} images for upload."}

@router.put(
    "/index-weights",
    summary="Update Index Weights Dict with int keys and float values",
    description="Endpoint to update index weights where the keys are integers and the values are floats."
)
async def update_index_weights(weights: Annotated[dict[str, float], Body(embed=True)]):
    return weights




