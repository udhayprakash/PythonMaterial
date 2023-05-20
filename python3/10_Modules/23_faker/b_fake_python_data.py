from faker import Faker

fake = Faker()

print(
    f"""
    {fake.pylist() =}
    {fake.pydict() =}
    {fake.pyint()  =}
"""
)
