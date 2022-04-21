from faker import Faker

fake = Faker()

print(f'''
    FAKE PERSONAL DETAIALS
    ----------------------
    {fake.name()}
    {fake.address()}
    {fake.job()}
    {fake.phone_number()}
    {fake.street_name()}
    {fake.city()}
    {fake.administrative_unit()}
    {fake.address()}

    {fake.text()}
    {fake.date_time()}
''')
