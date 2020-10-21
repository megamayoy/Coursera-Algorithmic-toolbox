# Uses python3
from math import floor


def get_majority_element(a, left, right):
    # if there's only one element in the array
    # then this element is the majority element
    if left == right:
        return a[left]

    middle = floor(left + (right - left) / 2)
    left_result = get_majority_element(a, left, middle)
    right_result = get_majority_element(a, middle+1, right)

    # if majority element in both sides are the same
    # then Horraaay this is majority element at the entire array level
    if left_result == right_result:
        return left_result

    array_size = right - left + 1
    counter_dict = dict.fromkeys([left_result, right_result], 0)
    # count occurrences
    for i in range(left, right+1):
        if a[i] == left_result:
            counter_dict[left_result] += 1
        if a[i] == right_result:
            counter_dict[right_result] += 1
    majority_element = -1
    if counter_dict[left_result] > array_size / 2:
        majority_element = left_result
    elif counter_dict[right_result] > array_size / 2:
        majority_element = right_result

    return majority_element


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)
