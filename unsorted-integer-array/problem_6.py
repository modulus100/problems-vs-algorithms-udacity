import random
import sys


def get_min_max(ints: list):
    if len(ints) == 0:
        raise Exception("cannot by empty")

    min = sys.maxsize
    max = -sys.maxsize

    for element in ints:
        if element < min:
            min = element
        if element > max:
            max = element

    return min, max


print("Test usual cases")
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

print("\nTest with negative numbers")
l = [i for i in range(-10, 11)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((-10, 10) == get_min_max(l)) else "Fail")


print("\nTest empty array")
try:
    get_min_max([])
except Exception:
    print("Pass")