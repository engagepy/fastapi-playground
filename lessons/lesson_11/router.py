from typing import Annotated, Literal
from fastapi import APIRouter, Query 

from pydantic import AfterValidator
import enum

router = APIRouter(
    prefix="/lesson-11",
    tags=["Lesson 11"]
)

