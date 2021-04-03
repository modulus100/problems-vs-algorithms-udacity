def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None or number < 0:
        raise Exception("Minimum number is 0")

    high = number
    low = 1

    while low <= high:
        middle = int((high + low) / 2)
        current = middle ** 2

        if current == number:
            return middle
        elif current < number:
            low = middle + 1
        elif current > number:
            high = middle - 1

    return high


print("Pass" if (3 == sqrt(9)) else "Fail")
# print("Pass" if (0 == sqrt(0)) else "Fail")
# print("Pass" if (4 == sqrt(16)) else "Fail")
# print("Pass" if (1 == sqrt(1)) else "Fail")
# print("Pass" if (5 == sqrt(27)) else "Fail")