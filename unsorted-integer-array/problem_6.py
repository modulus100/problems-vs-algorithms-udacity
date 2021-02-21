import random


def get_min_max(ints):
    min = ints[0]
    max = ints[0]

    for element in ints:
        if element < min:
            min = element
        if element > max:
            max = element

    return min, max


l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")