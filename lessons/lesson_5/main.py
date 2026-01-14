from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI(
    title="Lesson 5 - Query Parameter Validations",
    version="1.0.0",
    description="An example FastAPI application demonstrating query parameter validations using FastAPI's Query class."
    )

@app.get("/items/", tags=["Observe query parameter validations using FastAPI's Query class"])
async def read_items(q: Annotated[str | None, Query(max_length=20)] = None):
    results = {"items": [{"item_name": "Pizza"}, {"toppings": "Basil, Cheese, Tomato Sauce"}]}
    if q:
        results.update({"Extras": q})
    return results 
