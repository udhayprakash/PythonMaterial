from faker import Faker

fake_italian = Faker(locale='it_IT')
print('Italian:')
for _ in range(5):
    print('\t', fake_italian.name())

print()

fake_international = Faker(['it_IT', 'en_US', 'ja_JP'])
print('Italian + English + Japanese:')
for _ in range(5):
    print('\t', fake_international.name())
