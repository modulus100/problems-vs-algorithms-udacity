def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    last_index = len(input_list) - 1
    pivot = find_pivot(input_list, 0, last_index)

    if pivot == -1 or pivot == last_index:
        return binary_search(input_list, 0, last_index, number)
    if input_list[pivot] == number:
        return pivot
    if input_list[pivot] > number >= input_list[last_index]:
        return binary_search(input_list, 0, pivot - 1, number)
    return binary_search(input_list, pivot + 1, last_index, number)


def find_pivot(arr: list, start: int, end: int) -> int:
    if end < start:
        return -1
    if end == start:
        return start

    mid = int((start + end) / 2)
    if mid < end and arr[mid] > arr[mid + 1]:
        return mid
    if mid > start and arr[mid] < arr[mid - 1]:
        return mid - 1
    if arr[start] > arr[mid]:
        return find_pivot(arr, start, mid - 1)
    return find_pivot(arr, mid + 1, end)


def binary_search(arr: list, start: int, end: int, key: int) -> int:
    if start > end:
        return -1

    mid = int((start + end) / 2)
    if arr[mid] == key:
        return mid
    if arr[mid] > key:
        return binary_search(arr, start, mid - 1, key)
    return binary_search(arr, mid + 1, end, key)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


print("Test usual cases")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

print("\nTest empty array")
test_function([[], 9])

print("\nTest unshift array")
test_function([[1, 2, 3, 4, 5, 6, 7], 4])