import sys
INF = sys.maxint

"""
Given a list of N coins, their values
and the total sum S. Find the minimum number of coins the sum of which is S
(we can use as many coins of one type as we want), or
report that it's not possible to select coins in such a way that they sum up to S.
"""


def num_coins_td(coin_values, total_sum, memo):
    if memo[total_sum] is not None:
        return memo[total_sum]

    if total_sum == 0:
        memo[total_sum] = 0
        return 0

    min_coins = INF
    for v in coin_values:
        if total_sum-v >= 0 and \
                min_coins > 1 + num_coins_td(coin_values, total_sum - v, memo):
            min_coins = 1 + num_coins_td(coin_values, total_sum - v, memo)

    memo[total_sum] = min_coins
    return min_coins


def num_coins(coin_values, total_sum):

    min_coins = [INF for _ in range(total_sum + 1)]
    min_coins[0] = 0

    for si in range(1, total_sum + 1):
        for v in coin_values:
            if si-v >= 0 and min_coins[si] > 1 + min_coins[si-v]:
                min_coins[si] = 1 + min_coins[si-v]

    return min_coins[total_sum]


if __name__ == '__main__':
    V = [1, 3, 5]
    S = 11

    print(V, S, num_coins(V, S))

    memo = [None for _ in range(S+1)]
    print(V, S, num_coins_td(V, S, memo))
