from fastapi import APIRouter, Header
from pydantic import BaseModel
from typing import Annotated


router = APIRouter(
    prefix="/lesson-27",
    tags=["Lesson 27"]
)   


class CommonHeaders(BaseModel):
    model_config = {"extra": "forbid"}

    host: str
    save_data: str | None = None
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = None


@router.get(
    "/items",
    summary="Header Pydantic Model",
    description="Observe how to use Header parameters with a Pydantic model and forbid extra headers"
)
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers




