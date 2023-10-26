import random

coin = random.choice(["heads", "tails"])
print(coin)

#Using the specific library rather than a random one
from random import choice

coin = choice(["heads", "tails"])
print(coin)

#Using the randint module in random
import random

number = random.randint(1, 12)
print(number)

#Using the shuffle module in random
import random

cards = ["Ace of spades", "queen of spades", "ace of hearts", "king of diamonds", "jack of flowers"]
random.shuffle(cards)
for _ in cards:
    print(_)


#Using the statistics module in random
import statistics

print(statistics.mean([69, 57, 32, 29, 27, 25, 22]))