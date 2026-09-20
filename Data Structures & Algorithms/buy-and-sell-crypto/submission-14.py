class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l=0
        r=1

        maxP = 0
        while r < len(prices):
            profit = prices[r]-prices[l]
            maxP = max(maxP, profit)

            # what kind of condition to shrink the window and do like an l+=1

            if prices[r] < prices[l]:
                l=r

            r+=1

        return maxP
        