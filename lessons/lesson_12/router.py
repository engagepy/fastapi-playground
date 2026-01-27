from typing import Annotated, Literal
from fastapi import APIRouter, Query
from pydantic import BaseModel, Field
import enum
import random

router = APIRouter(
    prefix="/lesson-12",
    tags=["Lesson 12"]
)

