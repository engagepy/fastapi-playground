from fastapi import APIRouter
from pydantic import BaseModel, Field, HttpUrl

router = APIRouter(
    prefix="/lesson-19",
    tags=["Lesson 19"]
)

class Image(BaseModel):
    url : HttpUrl
    name : str

class User_Profile(BaseModel):
    username: str = Field(max_length=50)
    email: str = Field(max_length=100)
    image: list[Image]

class Group_Membership(BaseModel):
    group_name: str = Field(max_length=50)  
    user_profile: User_Profile


@router.post(
    "/group-membership",
    summary="Observe deeply nested models",
    description="Demonstrates how to use deeply nested models with special validation types like HttpUrl in FastAPI",
)
async def create_group_membership(membership: Group_Membership):
    return membership.model_dump()  
