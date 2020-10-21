# Uses python3
from math import floor


def merge(list_left, list_right):
    merge_list = []
    number_of_inversions = 0
    left_index = 0
    right_index = 0
    while left_index != len(list_left) and right_index != len(list_right):
        if list_left[left_index] > list_right[right_index]:
            merge_list.append(list_right[right_index])
            number_of_inversions += (len(list_left) - left_index)
            right_index += 1
        else:
            merge_list.append(list_left[left_index])
            left_index += 1

    while left_index != len(list_left):
        merge_list.append(list_left[left_index])
        left_index += 1

    while right_index != len(list_right):
        merge_list.append(list_right[right_index])
        right_index += 1

    return number_of_inversions, merge_list


def get_number_of_inversions(a, left, right):
    number_of_inversions = 0
    if right == left:
        return number_of_inversions, [a[left]]
    middle = floor(left + (right - left) / 2)
    left_number_of_inversions, left_branch = get_number_of_inversions(
        a, left, middle
    )
    right_number_of_inversions, right_branch = get_number_of_inversions(
        a, middle + 1, right
    )

    merge_inversions, sorted_list = merge(left_branch, right_branch)
    number_of_inversions = (
        left_number_of_inversions
        + right_number_of_inversions
        + merge_inversions
    )
    return number_of_inversions, sorted_list


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(get_number_of_inversions(a, 0, len(a)-1)[0])
