from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    price: float
    description: str = None


items = []


@app.get("/items")
async def get_items():
    return items


@app.post("/items")
async def create_item(item: Item):
    items.append(item)
    return item


@app.get("/items/{id}")
async def get_item(id: int):
    for item in items:
        if item.id == id:
            return item
    return {"error": "item not found"}


@app.put("/items/{id}")
async def update_item(id: int, item: Item):
    for index, stored_item in enumerate(items):
        if stored_item.id == id:
            items[index] = item
            return {"message": "item updated"}
    return {"error": "item to update not found"}


@app.delete("/items/{id}")
async def delete_item(id: int):
    for index, stored_item in enumerate(items):
        if stored_item.id == id:
            del items[index]
            return {"message": "item deleted"}
    return {"error": "item to delete not found"}
