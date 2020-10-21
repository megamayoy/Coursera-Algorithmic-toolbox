# Uses python3
import sys


def gcd_euclidean_algorithm(a, b):
    x = min(a, b)
    y = max(a, b)
    while x != 0:
        modulus = y % x
        y = x
        x = modulus
    return y


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

# lcm(a,b) = |a * b| / gcd(a,b)
# corner case lcm(0,0) = 0


def lcm_using_gcd(a, b):
    if a == 0 and b == 0:
        return 0
    temp = a / gcd_euclidean_algorithm(a, b)
    return int(b * temp)


if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    print(lcm_using_gcd(a, b))
