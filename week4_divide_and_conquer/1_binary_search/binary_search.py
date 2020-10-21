# Uses python3
import math


def binary_search(a, left, right, x):
    # base case
    if left > right:
        return -1
    middle = math.floor(left + (right - left) / 2)
    if a[middle] == x:
        return middle
    if a[middle] > x:
        # branch left
        result = binary_search(a, left, middle-1, x)
    else:
        # branch right
        result = binary_search(a, middle+1, right, x)

    return result


if __name__ == '__main__':
    search_list = input()
    search_queries = input()
    search_list = list(map(int, search_list.split()))
    search_queries = list(map(int, search_queries.split()))
    list_length = search_list[0]
    num_of_queries = search_queries[0]

    search_list = search_list[1:]
    search_queries = search_queries[1:]
    for query in search_queries:
        print(binary_search(search_list, 0, list_length - 1, query), end=' ')
