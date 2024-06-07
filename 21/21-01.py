import random
from pprint import pprint


def make_bingo():
    numbers = random.sample(range(1, 76), 25)
    numbers[12] = 0
    return tuple(tuple(numbers[i: i+5]) for i in range(0, 25, 5))


pprint(make_bingo())