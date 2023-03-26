from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello():
    return {"Hello": "World"}


@app.get("/component/{component_id}")  # path paramters
async def get_component(component_id: int):
    return {"component_id": component_id}


@app.get("/component/")  # query parameters
async def read_component(number: int, text: Optional[str]):
    """query params"""
    return {"number": number, "text": text}


# python -m uvicorn project1:app --reload


# http://127.0.0.1:8000/openapi.json
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

"""`
~!curl 127.0.0.1:8000/
{"Hello":"World"}
~!curl 127.0.0.1:8000/component/
{"detail":"Not Found"}
~!curl 127.0.0.1:8000/component/udhay
{"component_id":"udhay"}
~!curl 127.0.0.1:8000/component/something
{"component_id":"something"}


http://127.0.0.1:8000/component/?number=213121&text=sadsds
"""
