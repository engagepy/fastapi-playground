from fastapi import APIRouter, Header
from pydantic import BaseModel
from typing import Annotated


router = APIRouter(
    prefix="/lesson-25",
    tags=["Lesson 25"]
)

