from fastapi import APIRouter, Body
from pydantic import BaseModel, Field, HttpUrl
from typing import Annotated


router = APIRouter(
    prefix="/lesson-18",    
    tags=["Lesson 18"]
)

class Image(BaseModel):
    url : HttpUrl
    name : str

class User_Profile(BaseModel):
    username: str = Field(default="johndoe", example="johndoe", max_length=50)
    email: str = Field(default=" ", example="jd@jd.com", max_length=100)
    image: list[Image]



@router.post(
    "/profile/{user_id}/image",
    summary="Observe special Pydantic types and additional validation via Field() in nested models",
    description="Demonstrates how to use Body() to accept a Pydantic model with nested models in the request body while also accepting path parameters for adding an image to a user profile",  
)
async def add_profile_image(
    user_id: Annotated[int, Field(title="User ID", description="The ID of the user profile to add an image to", gt=0)],
    profile: Annotated[User_Profile, Body(embed=True)]
):
    return {
        "user_id": user_id,
        "image": profile.model_dump()
    }   
