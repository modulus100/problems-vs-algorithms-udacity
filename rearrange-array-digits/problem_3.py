import queue


class Node:
    def __init__(self, val: int):
        self.val = val

    def __gt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def __str__(self):
        return "val: " + str(self.val)


def rearrange_digits(input_list: list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None:
        raise Exception("input is not valid")

    p_queue = queue.PriorityQueue()

    for element in input_list:
        p_queue.put(Node(element))

    i = 0
    first_number = 0
    second_number = 0
    first_flag = True

    while not p_queue.empty():
        node: Node = p_queue.get()
        if first_flag:
            first_number += node.val * 10 ** i
        else:
            second_number += node.val * 10 ** i
            i += 1
        first_flag = not first_flag
    return [first_number, second_number]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


print("Test usual cases")
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[9, 2, 5, 6, 0, 4], [952, 640]])

print("\nTest empty array")
test_function([[], [0, 0]])

print("\nTest invalid input")
try:
    test_function([None, [0, 0]])
except Exception:
    print("Pass")