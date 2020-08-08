"""
121. Best Time to Buy and Sell Stock


Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.



Input: [7,1,5,3,6,4]
        \   |
        m = 5
            
        
 max = -inf 
 
 max_n = max(max_n,n - n-1 )
 

Output: 5



Understand:
--> each iteration we are trying to find out the global minimum vlaue stock 
--> if the current price is less than the current minimum then we overwrite the current minimum with the current price.
--> When ever the current price is greater than the current minimum then we check if the m,ax profit is bigger than the curent profit. the current profit is the current price - the minimum value 
--> we use max method to acheive this 
--> after we need to return max_profit after the loop is over 

Match:
pointers 
max 
\


Time complexity : O(n) where n is the length of the input array 
space: O(1)
"""


class Solution:
    def maxProfit(self, prices):

        min_value = float("inf")
        max_profit = 0

        for curr_price in prices:
            print(min_value)
            print(max_profit)

            """
            Input: [7,1,5,3,6,4]
                            \   
                    min = 1
                    max = 5
        
            
            """
            if curr_price < min_value:
                min_value = curr_price
            else:
                max_profit = max(max_profit, curr_price - min_value)

        return max_profit
