# Uses python3

import sys


def lcs2(a, b):
    # create dp table
    two_d_dp = []
    for i in range(0, len(a) + 1):
        two_d_dp.append([0] * (len(b) + 1))

    for i in range(0, len(a)+1):
        for y in range(0, len(b)+1):
            if i == 0 or y == 0:
                continue
            if a[i-1] == b[y-1]:
                two_d_dp[i][y] = max(
                    1 + two_d_dp[i-1][y-1],
                    two_d_dp[i][y-1],
                    two_d_dp[i-1][y]
                )
            else:
                two_d_dp[i][y] = max(
                    two_d_dp[i][y-1],
                    two_d_dp[i-1][y]
                )
    return two_d_dp[len(a)][len(b)]


if __name__ == '__main__':

    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    print(lcs2(a, b))
