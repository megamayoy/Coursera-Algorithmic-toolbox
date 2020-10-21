# Uses python3
import sys


def optimal_weight(knapsack_weight, bars_weights, number_of_gold_bars):
    dp = []
    for _ in range(0, knapsack_weight + 1):
        dp.append([0] * (len(bars_weights) + 1))

    for w in range(0, knapsack_weight + 1):
        for bar_index in range(0, number_of_gold_bars + 1):
            # you can either take or leave the current bar
            if w == 0 or bar_index == 0:
                continue
            # leave option
            max_weight = dp[w][bar_index-1]
            current_bar_weight = bars_weights[bar_index - 1]
            if current_bar_weight <= w:
                # take option
                max_weight = max(
                    max_weight,
                    current_bar_weight + dp[w-current_bar_weight][bar_index-1]
                )
            dp[w][bar_index] = max_weight

    return dp[knapsack_weight][number_of_gold_bars]


if __name__ == '__main__':

    knapsack_weight, number_of_gold_bars = map(int, input().split())
    bars_weights = list(map(int, input().split()))

    print(optimal_weight(knapsack_weight, bars_weights, number_of_gold_bars))
