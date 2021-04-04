def sort_012(input_list: list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list is None:
        raise Exception("input is not valid")

    i = 0
    mid = 0
    k = len(input_list) - 1

    while mid <= k:
        if input_list[mid] == 0:
            input_list[i], input_list[mid] = input_list[mid], input_list[i]
            i += 1
            mid += 1
        elif input_list[mid] == 1:
            mid += 1
        else:
            input_list[mid], input_list[k] = input_list[k], input_list[mid]
            k -= 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


print("Test usual cases")
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

print("\nTest empty array")
test_function([])

print("\nTest invalid input")
try:
    test_function(None)
except Exception:
    print("Pass")