# coin -- head/tail
import random

outcomes = {
    "heads": 0,
    "tails": 0,
}
sides = list(outcomes.keys())  # ['heads', 'tails']


for i in range(10000):
    outcome = random.choice(sides)
    outcomes[outcome] += 1

print("In 10000 tosses,")
print("\tHeads:", outcomes["heads"])
print("\tTails:", outcomes["tails"])
