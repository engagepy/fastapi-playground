from typing import Annotated
from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel, Field
import enum

router = APIRouter(
    prefix="/lesson-17",
    tags=["Lesson 17"]
)

class ProfessionalDetails(BaseModel):
    company: str = Field(default="Tech Company", example="Tech Company", max_length=100)
    position: str = Field(default="Software Engineer", example="Software Engineer", max_length=100)

class ContactCard(BaseModel):
    name: str = Field(default="John Doe", example="John Doe", max_length=100)
    email: list[str] = set() 
    phone: list[str] = set()
    address: str = Field(default="123 Main St, Anytown, USA", example="123 Main St, Anytown, USA", max_length=200)
    professional_details: ProfessionalDetails

@router.post(
        "/contact-card/{card_id}",
        summary="Create a Contact Card with Nested Pydantic Models and unique email and phone numbers via `sets`",
        description="Demonstrates how to use Body() to accept a Pydantic model with nested models in the request body while also accepting path parameters for creating a contact card, ensuring unique email and phone numbers using `sets`",
        )
async def create_contact_card(
    card_id: Annotated[int, Path(title="Card ID", description="The ID of the contact card", gt=0)],
    contact_card: Annotated[ContactCard, Body(title="Contact Card", description="The details of the contact card to create with nested professional details")]
):
    return {
        "card_id": card_id,
        "contact_card": contact_card.model_dump()
    }   

