class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        l = 0
        r = 1


        profit = 0
        while r < len(prices):
            money = prices[r]-prices[l]

            profit = max(profit, money)


            if (prices[l] > prices[r]):
                l=r

            r+=1



        return profit
        