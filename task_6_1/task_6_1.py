import numpy as np

def DPChange(money, coins):
    min_num_coins = [None]*(money+1)
    min_num_coins[0] = 0
    for m in range(1,money+1):
        min_num_coins[m] = 1000000
        for i in range(0,len(coins)):
            if m >= int(coins[i]):
                if (min_num_coins[m-int(coins[i])]+1)<min_num_coins[m]:
                    min_num_coins[m] = min_num_coins[m-int(coins[i])]+1
    return min_num_coins[money]

money = int(input())
coins = input().split()
print(DPChange(money, coins))
