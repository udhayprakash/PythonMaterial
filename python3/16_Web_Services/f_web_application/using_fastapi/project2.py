from fastapi import FastAPI, HTTPException

app = FastAPI()

cache = [{"fruit": "mango"}, {"fruit": "apple"}]  # O(N)

# cache = {
#     "fruit": "mango",   # O(1)
# }


@app.get("/")
async def default_endpoint():
    return {"status": "Hellowold"}


@app.get("/cache")
async def cache_endpoint():
    return {"cache": cache}


@app.post("/cache")
async def cache_add(key, value):
    if {key: value} in cache:
        return {"status": "Already existng", "cache": cache}

    cache.append({key: value})
    return {"status": "Added Item", "cache": cache}


@app.delete("/cache")
async def cache_delete(key, value):
    for record in cache:
        if {key: value} == record:
            cache.remove(record)
            return {"status": "delete an element", "cache": cache}
    return HTTPException(status_code=404, detail="Item not found")


# python -m uvicorn project1:app --reload
