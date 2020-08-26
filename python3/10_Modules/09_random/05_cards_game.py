## SHUFFLING A DECK OF CARDS
## A deck of cards has 13 cards each of 4 suits: heart(♥), spade(♠), diamond(♦), club(♣).
## THOUGHT PROCESS: Construct an unshuffled deck by using two lists, one for suits, another for cardValues -> Shuffle the deck by iterating over all cards one by one using their indexes, and swapping the index with any random index.
 
import random
 
suits = ["♠", "♥", "♦", "♣"]
cardValues = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
 
# initializing an empty deck
deck = []
 
# CONSTRUCTING AN UNSHUFFLED DECK
for suit in suits:
    for value in cardValues:
        deck.append(value + suit)
# printing the unshuffled deck
print("The original deck of cards:\n\n", deck)
 
 
# SHUFFLING CARDS: iterating over all cards one by one using their indexes, swapping the index with any random index
# Iterate over all cards one by one using their indexes
for index in range(0, len(deck)):
    randomCardForSwitching = random.randrange(len(deck))   
    # Swapping indexes
    temporaryIndex = deck[index]
    deck[index] = deck[randomCardForSwitching]
    deck[randomCardForSwitching] = temporaryIndex
# printing the shuffled deck
print("\nThe shuffled deck of cards:\n\n", deck)
