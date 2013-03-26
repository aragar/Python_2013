COINS = (100, 50, 20, 10, 5, 2, 1)


def calculate_coins(sum):
    sum *= 100
    dict = {}
    for coin in COINS:
        dict[coin] = sum // coin
        sum -= dict[coin] * coin
    return dict
