# Uses python3
import sys


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_euclidean_algorithm(a, b):
    x = min(a, b)
    y = max(a, b)
    while x != 0:
        modulus = y % x
        y = x
        x = modulus
    return y


if __name__ == "__main__":
    input = input()
    a, b = map(int, input.split())
    print(gcd_euclidean_algorithm(a, b))
