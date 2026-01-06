# Leet Code # 121

class Solution:
    def bestTimeToBuyAndSellStock(self, prices: List[int]) -> int:
        # Brute Force Approach  It has time complexity of O(N^2) which will not pass the test cases in leetCode  Space: O(1)
        # max_profit = float('-inf') # '-inf' is negative infinity
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
                
        #         if profit > 0:
        #             max_profit = max(max_profit, profit)
                    
        # return max_profit if max_profit > float('-inf') else 0
    
    
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
                
            profit = price - min_price
            
            if profit > max_profit:
                max_profit = profit
                
        return max_profit