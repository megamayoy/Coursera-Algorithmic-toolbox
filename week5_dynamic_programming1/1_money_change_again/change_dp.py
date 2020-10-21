# Uses python3
import sys

DENOMINATIONS = [1, 3, 4]


def get_change(m):
    memorize = [0] * (m + 1)
    # initialize array

    for index, _ in enumerate(memorize):
        # print(index)
        if index == 0:
            continue
        min_coins = float("inf")
        for d in DENOMINATIONS:
            if d <= index:
                min_coins = min(min_coins, 1 + memorize[index-d])
        memorize[index] = min_coins
    return memorize[m]


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
