"""
    buy-sell
    [7, 1, 5, 3, 6, 4] ==> 5 --> best time to buy is 1 and best time to sell is 5
    [9, 7, 6, 4, 3, 1] ==> 0 --> There has never been a good time to buy

"""

def max_profit(price):
    best = 0
    result = 0
    for i in range(1,len(price)):
        cur = price[i] - price [i - 1]
        if  best < cur:
            best = cur
            result = price [i]
            
    return result 

