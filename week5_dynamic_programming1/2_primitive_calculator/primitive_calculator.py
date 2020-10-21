# Uses python3
import sys


def prim_cal_dp(n):
    dp_table = [float("inf")] * (n+1)
    dp_table[0] = 0
    dp_table[1] = 0
    for i in range(2, n+1):
        min_opts = float("inf")
        if i % 3 == 0:
            min_opts = min(min_opts, 1 + dp_table[i//3])
        if i % 2 == 0:
            min_opts = min(min_opts, 1 + dp_table[i//2])
        min_opts = min(min_opts, 1 + dp_table[i-1])
        dp_table[i] = min_opts
    return dp_table


def optimal_sequence(n, dp_table):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0 and dp_table[n] == 1 + dp_table[n//3]:
            n = n // 3
        elif n % 2 == 0 and dp_table[n] == 1 + dp_table[n//2]:
            n = n // 2
        else:
            n = n-1
    return reversed(sequence)


n = int(input())
# print(prim_calc_wrapper(n))
dp_table = prim_cal_dp(n)
print(dp_table[n])

sequence = list(optimal_sequence(n, dp_table))
for x in sequence:
    print(x, end=' ')
