from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI(
    title="Lesson 6 - Multiple Query Parameters with Validations",
    version="1.0.0",
    description="An example FastAPI application demonstrating multiple query parameters with uniform validation using FastAPI's Query class."
    )

@app.get("/items/", tags=["Observe multiple query parameter validations using list[str] within FastAPI's Query class"])
async def read_items(q: Annotated[list[str] | None, Query(max_length=20)] = None):
    results = {"items": [{"item_name": "Pizza"}, {"toppings": "Basil, Cheese, Tomato Sauce"}]}
    if q:
        results.update({"Extras": q})
    return results 
