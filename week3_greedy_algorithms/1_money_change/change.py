# Uses python3
import sys
import math


def get_change(m):
    # write your code here
    denominations = [10, 5, 1]
    d = 0
    number_of_denominations = 3
    minimum_number_of_coins = 0
    while d < number_of_denominations and m != 0:
        if m >= denominations[d]:
            changed_coins = math.floor(m / denominations[d])
            m = m % denominations[d]
            minimum_number_of_coins += changed_coins
        d += 1
    return minimum_number_of_coins


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
