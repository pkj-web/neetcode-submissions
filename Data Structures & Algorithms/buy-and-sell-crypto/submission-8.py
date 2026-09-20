class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0


        l = 0

        r=1


        while r < len(prices):
            money = prices[r] - prices[l]
            profit = max(profit, money)


            if prices[l]>=prices[r]:
                l=r

            r+=1


        return profit
        