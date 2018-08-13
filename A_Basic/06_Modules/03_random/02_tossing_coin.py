import random

outcomes = {
    'heads': 0,
    'tails': 0,
}
sides = outcomes.keys()  # ['heads', 'tails']

for i in range(10000):
    outcomes[random.choice(sides)] += 1

print 'In 10000 tosses,'
print '\tHeads:', outcomes['heads']
print '\tTails:', outcomes['tails']
