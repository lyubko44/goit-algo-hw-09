from collections import defaultdict

nominal = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(total_sum, nominal):
    grouped_by_nom = defaultdict(int)

    while total_sum > 0:
        for nom in nominal:
            if nom <= total_sum:
                total_sum -= nom
                grouped_by_nom[nom] += 1
                break

    return dict(grouped_by_nom)

print("greedy:", find_coins_greedy(113, nominal))    

def find_min_coins(m, coins):
    min_coins = [float('inf')] * (m + 1)
    coin_used = [0] * (m + 1)
 
    min_coins[0] = 0

    for i in range(1, m + 1):
        for coin in coins:
            if i - coin >= 0 and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    result = defaultdict(int)
    current = m
    while current > 0:
        coin = coin_used[current]
        result[coin] += 1
        current -= coin

    return dict(result)

print("dp:", find_min_coins(113, nominal))    