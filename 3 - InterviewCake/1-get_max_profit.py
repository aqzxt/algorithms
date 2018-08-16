"""
Created on Thu Feb  1 04:21:15 2018 ----------- @author: mxhfield

"""

def get_max_profit(stock_prices):
    
    if len(stock_prices) < 2:
        raise ValueError
        
    min_value, max_value = stock_prices[0], stock_prices[1]
    
    # Calculate the max profit
    for e in range(len(stock_prices)-1):
        
        if stock_prices[e] < min_value:
            min_value = stock_prices[e]
            
        if stock_prices[e+1] > max_value:
            max_value = stock_prices[e+1]
            
    print(max_value, min_value)
    if max_value - min_value <= 0:
        return 0
    return max_value - min_value



# Add some more tests

test_input = [10, 7, 5, 11, 9]
print('{} should be {}'.format(get_max_profit(test_input), 6))

def maxProfit(A):
    total=0
    for i in range(0,len(A)-1):
        print(total)
        
        if A[i+1] > A[i]:
            total += A[i+1] - A[i]
    return total

#print(maxProfit([1, 2, 3]))
print(maxProfit([10, 7, 5, 11, 9]))