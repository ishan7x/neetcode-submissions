class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # I will start on day 1 on my left and tryt o find min from left while sell is from right looking for the max until buy <= sell. The max profit so far is the answer
        buy = 0
        sell = 1
        maxP = 0
        while (sell < len(prices)):
            if (prices[buy] < prices[sell]):
                currP = prices[sell] - prices[buy]
                print(prices[buy], prices[sell])
                maxP = max(maxP, currP) 
            else:
                buy = sell
            sell += 1
        return maxP
        