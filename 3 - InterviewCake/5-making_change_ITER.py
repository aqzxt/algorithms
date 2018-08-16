"""
Created on Sun Feb 11 02:12:38 2018 ----------- @author: mxhfield

"""

def change_possibilities_bottom_up(amount, denominations):
    ways = [0] * (amount + 1)
    ways[0] = 1

    for coin in denominations:
        for higher_amount in range(coin, amount +1):
            higher_amount_remainder = higher_amount - coin
            ways[higher_amount] += ( ways[higher_amount_remainder] )
            
            print(higher_amount, '===',higher_amount_remainder, '===',ways)
    return ways[amount]


# run your function through some test cases here
# remember: debugging is half the battle!
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(change_possibilities_bottom_up(14, d))
