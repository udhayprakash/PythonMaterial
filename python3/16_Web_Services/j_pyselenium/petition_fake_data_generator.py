import csv
import random

from faker import Faker
from faker.providers import address

fake = Faker()
fake.add_provider(address)

# create a list of country names
countries = [
    "USA",
    "Canada",
    "India",
    "Japan",
    "Australia",
    "China",
    "Germany",
    "France",
    "Brazil",
    "Mexico",
]


# function to generate valid postcode for a given country
def generate_postcode(country):
    if country in ["USA", "Canada"]:
        return fake.postcode()
    elif country == "India":
        return fake.postcode_in_state(state_abbr="IN")
    elif country == "Japan":
        return fake.postcode_in_prefecture(prefecture="Tokyo")
    elif country == "Australia":
        return fake.postcode_in_state_or_territory(state_abbr=None, territory_abbr=None)
    elif country == "China":
        return fake.postcode_in_subdivision(subdivision="Beijing")
    elif country in ["Germany", "France"]:
        return fake.postcode_in_state(state_abbr=None)
    elif country in ["Brazil", "Mexico"]:
        return fake.postcode_in_state(state_abbr=None, city=None)


# generate 10 records of dummy data
data = []
for i in range(10):
    country = random.choice(countries)
    postcode = generate_postcode(country)
    record = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "postcode": postcode,
        "country": country,
    }
    data.append(record)

# save the data to a CSV file
with open("petetion_dummy_data.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(
        file, fieldnames=["first_name", "last_name", "email", "postcode", "country"]
    )
    writer.writeheader()
    writer.writerows(data)

print("Data saved to petetion_dummy_data.csv")
