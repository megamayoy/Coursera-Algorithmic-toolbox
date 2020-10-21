# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit(n):
    if n <= 1:
        return n
    x = 0
    y = 1
    z = 0
    for _ in range(2, n+1):
        z = (x + y) % 10
        x = y
        y = z
    return z


if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))
