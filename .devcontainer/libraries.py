import random

coin = random.choice(["heads", "tails"])
print(coin)

#Using the specific library rather than a random one
from random import choice

coin = choice(["heads", "tails"])
print(coin)

#Using the randint module random
import random

number = random.randint(1, 12)
print(number)