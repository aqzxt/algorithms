"""
Created on Sun Feb 11 02:12:38 2018 ----------- @author: mxhfield

"""

def change_possib_top_down(amount_left, denom, current_index=0, memo={}):
    # Memoization in recursion:
    # concludes in a return statement rather than skiping a call
    memo_key = (amount_left, current_index)
    if memo_key in memo:
        return memo[memo_key]
    
    # Base cases:
    # We hit the amount spot on. yes!
    if amount_left == 0:
        return 1

    # We overshot the amount left (used too many coins)
    if amount_left < 0:
        return 0

    # We're out of denominations
    if current_index == len(denom):
        return 0

    print("checking ways to make %i with %s" % (
            amount_left, denom[current_index:],))

    # Choose a current coin
    current_coin = denom[current_index]

    # See how many possibilities we can get
    # for each number of times to use current_coin
    num_possib = 0
    while amount_left >= 0:
        num_possib += change_possib_top_down(
                amount_left, denom, current_index + 1,)
        amount_left -= current_coin
    
    memo[memo_key] = num_possib
    return num_possib

# run your function through some test cases here
# remember: debugging is half the battle!
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(change_possib_top_down(14, d))
