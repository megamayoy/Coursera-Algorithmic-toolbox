# Uses python3
import sys
from operator import itemgetter


def get_optimal_value(capacity, weights, values):
    max_value = 0.
    # construct list of tuples. each tuple is ( (vi/wi) , index of ith item)
    items = []
    for i in range(len(weights)):
        items.append((values[i] / weights[i], i))
    # sort the values in decreasing order
    sorted_items = sorted(items, key=itemgetter(0), reverse=True)
    current_item_index = 0
    while capacity != 0 and current_item_index < len(items):
        kgs_taken = min(capacity, weights[sorted_items[current_item_index][1]])
        capacity -= kgs_taken
        max_value += (kgs_taken * sorted_items[current_item_index][0])
        current_item_index += 1
    return max_value


if __name__ == "__main__":
    # data = list(map(int, sys.stdin.read().split()))
    # n, capacity = data[0:2]
    # values = data[2:(2 * n + 2):2]
    # weights = data[3:(2 * n + 2):2]

    n, capacity = map(int, input().split())
    items = []
    weights = []
    values = []
    for i in range(n):
        v, w = map(int, input().split())
        values.append(v)
        weights.append(w)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
