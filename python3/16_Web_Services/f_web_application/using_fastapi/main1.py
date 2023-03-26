from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# py -m uvicorn main1:app --reload

# Browser               --> http://127.0.0.1:8000
# swagger               --> http://127.0.0.1:8000/docs
# swagger(alternative)  --> http://127.0.0.1:8000/redoc
# openAPI               --> http://127.0.0.1:8000/openapi.json
