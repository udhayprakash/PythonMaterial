"""
BATCH - How it works
async def get_location(address)
    1. Put the address on a queue of requests.
    2. Start a background task that:
        i. Waits a short time for other requests to be enqueued.
        ii. Processes all queued requests as a batch.
        iii. Notifies the waiting 'get_location' functions.
    3. Wait for the result and return it.

"""
import asyncio
import json
from urllib.parse import urlencode

import aiohttp

# Constants for accessing the Geoapify batch API
GEOCODING_BATCH_API = "https://api.geoapify.com/v1/batch/geocode/search"
YOUR_API_KEY = "xxxx-xxxx-xxxx-xxxx"


async def get_locations(addresses):
    """Return a dictionary of address -> (lat, lon)."""
    # Construct the URL to do the batch request
    query_string = urlencode({"apiKey": YOUR_API_KEY})
    url = f"{GEOCODING_BATCH_API}?{query_string}"

    # Build the JSON payload for the batch POST request
    data = json.dumps(addresses)

    # And use Content-Type: application/json in the headers
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    # Make the POST request to the API
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, headers=headers) as response:
            response_json = await response.read()
            response_data = json.loads(response_json)

    # The API can return a dict with a pending status if it needs more
    # time to complete. Poll the API until the result is ready.
    while isinstance(response_data, dict) and response_data.get("status") == "pending":
        # Wait a bit before calling the API
        await asyncio.sleep(0.1)

        # Query the result to see if it's ready yet
        request_id = response_data.get("id")
        async with aiohttp.ClientSession() as session:
            async with session.get(url + f"&id={request_id}") as response:
                response_json = await response.read()
                response_data = json.loads(response_json)

    # Gather the results into a dictionary of address -> (lat, lon)
    locations = {}
    for result in response_data:
        address = result["query"]["text"]
        coords = result["lat"], result["lon"]
        locations[address] = coords

    return locations
