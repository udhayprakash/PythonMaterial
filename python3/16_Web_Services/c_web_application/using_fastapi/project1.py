from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def hello():
    return {'Hello': 'World'}


# python -m uvicorn project1:app --reload


# http://127.0.0.1:8000/openapi.json
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc


# curl 127.0.0.1:8000/
# {"Hello": "World"}
