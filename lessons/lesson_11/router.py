from typing import Annotated, Literal
from fastapi import APIRouter, Query 

from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/lesson-11",
    tags=["Lesson 11"]
)


class MovieRequest(BaseModel):
    model_config = {"extra": "forbid"}  # to forbid extra fields in the request body
    title: str = Field(..., title="Movie Title", max_length=100)
    director: str = Field(..., title="Director Name", max_length=50)
    year: int = Field(..., title="Release Year", ge=1900, le=2100)

@router.get(
    "/get_movie/",
    summary="Path parameter validation using Literal and AfterValidator",
    description="Demonstrates path parameter validation using Literal from typing and BaseModel, Field from Pydantic."
)

# for beginners `q` is query parameter here and acting as request body via MovieRequest pydantic model defined above
async def find_movie(
    q: Annotated[MovieRequest, Query(title="Movie details in the request body")]
):
    return {"movie" : q.model_dump()}

