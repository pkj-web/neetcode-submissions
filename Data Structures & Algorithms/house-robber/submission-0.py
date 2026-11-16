class Solution:
    def rob(self, nums: List[int]) -> int:
        

        # DP problem
        moneyMax = 0

        n=len(nums)

        dp = [0] * (n+1) # ex2: [0,0,0,0,0,0]

        # gonna need me dp base cases though:

        dp[0] = nums[0] # the maximum amount of money we can rob

        for i in range(1,n):

            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        
        return dp[n-1] 