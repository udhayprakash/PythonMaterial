import time

import requests
from bs4 import BeautifulSoup

while True:
    # Make a request to the website
    response = requests.get("https://www.worldometers.info/coronavirus/")

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the element containing the number of COVID cases
    cases = soup.find_all("div", {"class": "maincounter-number"})[0].span.text.strip()

    # Print the number of COVID cases
    print(f"Number of COVID cases: {cases}")

    # Wait for one minute before refreshing the data
    time.sleep(60)
