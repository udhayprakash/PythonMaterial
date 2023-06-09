import asyncio
import json
from urllib.parse import urlencode

import aiohttp

# Test data
STREET_ADDRESSES = [
    "1600 Pennsylvania Avenue, Washington DC, USA",
    "11 Wall Street New York, NY",
    "350 Fifth Avenue New York, NY 10118",
    "221B Baker St, London, England",
    "Tour Eiffel Champ de Mars, Paris",
    "4059 Mt Lee Dr.Hollywood, CA 90068",
    "Buckingham Palace, London, England",
    "Statue of Liberty, Liberty Island New York, NY 10004",
    "Manger Square, Bethlehem, West Bank",
    "2 Macquarie Street, Sydney",
]
# Constants for accessing the Geoapify API
GEOCODING_API = "https://api.geoapify.com/v1/geocode/search"
YOUR_API_KEY = "xxxx-xxxx-xxxx-xxxx"


async def get_location(address):
    """Return (latitude, longitude) from an address."""
    # Construct the URL to do the lookup for a single address
    query_string = urlencode(
        {"apiKey": YOUR_API_KEY, "text": address, "limit": 1, "format": "json"}
    )
    url = f"{GEOCODING_API}?{query_string}"
    # Make the request to the API
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            # Read the json string and return the latitude and longitude
            # from the first result (there will only be one)
            results = json.loads(data.decode())["results"]
            return results[0]["lat"], results[0]["lon"]


# async def main():
#     # Print the city for each IP address
#     tasks = []
#     for address in STREET_ADDRESSES:
#         location = await get_location(address)
#         print(f"{address} -> {location}")


async def main():
    # Get the location for each address
    tasks = []
    for address in STREET_ADDRESSES:
        tasks.append(get_location(address))
    # Wait for all tasks to complete
    locations = await asyncio.gather(*tasks)
    # Print them all once all requests have completed
    for address, location in zip(STREET_ADDRESSES, locations):
        print(f"{address} -> {location}")


# Because it's an async function you need to run it using the asyncio event loop
loop = asyncio.new_event_loop()
loop.run_until_complete(main())
