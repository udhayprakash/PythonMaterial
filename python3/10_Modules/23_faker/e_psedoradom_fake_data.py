import random

import pandas as pd
from faker import Faker

Faker.seed(0)
random.seed(0)
fake = Faker("de_DE")

name, city_name, country, job, age = [[] for k in range(0, 5)]
for row in range(0, 100):
    name.append(fake.name())
    city_name.append(fake.city_name())
    country.append(fake.country())
    job.append(fake.job())
    age.append(random.randint(20, 100))

d = {"Name": name, "Age": age, "City": city_name, "Country": country, "Job": job}
df = pd.DataFrame(d)
print(df.head())
