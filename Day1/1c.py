#You are given an array prices where prices[i] is the price of a stock on day i. You want to maximise profit by choosing a single day to buy and a different later day to sell. Return the maximum profit. If no profit is possible return 0.
def max_profit(prices):
    min_profit=float('inf')
    max_profit=0
    for i in prices:
        if i<min_profit:
            min_profit=i
        elif i-min_profit>max_profit:
            max_profit=i-min_profit
    return max_profit
print(max_profit([7,1,5,3,6,4])) 
print(max_profit([7,6,4,3,1]))
print(max_profit([1,2]))