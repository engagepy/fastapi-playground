from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import Annotated 
from uuid import UUID
from datetime import datetime, time, timedelta


router = APIRouter(
    prefix="/lesson-23",
    tags=["Lesson 23"]
)


@router.post(
        "/items/{item_id}",
        summary="Create an Item with datetime and timedelta",
        description="Observe how to use datetime and timedelta in the OpenAPI docs"
        )
async def post_item(
    item_id: UUID,
    start_datetime: Annotated[datetime, Body()],
    end_datetime: Annotated[datetime, Body()],
    process_after: Annotated[timedelta,Body()],
    repeat_at: Annotated[time | None, Body()] = None, #optional time field for repeating the process, default is None
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_datetime
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration.total_seconds(), #human readable duration in seconds
        "repeat_at": repeat_at
        }
