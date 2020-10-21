# Uses python3
def calc_fib_recursive(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib(n):
    if (n <= 1):
        return n
    x = 0
    y = 1
    z = 0
    for _ in range(2, n+1):
        z = x + y
        x = y
        y = z

    return z


n = int(input())
print(calc_fib(n))
