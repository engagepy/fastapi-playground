from typing import Annotated
from fastapi import APIRouter, Cookie
from pydantic import BaseModel


APIRouter = APIRouter( 
    prefix="/lesson-26", 
    tags=["Lesson 26"]
)

