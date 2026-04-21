from fastapi import APIRouter, Header
from pydantic import BaseModel
from typing import Annotated


router = APIRouter(
    prefix="/lesson-27",
    tags=["Lesson 27"]
)   


