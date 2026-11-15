class Solution:
    def climbStairs(self, n: int) -> int:
        # doing a bottom up approach using tabulation/iteration

        # 1. Create DP array
        dp = [0] * (n + 1)

        # 2. Initialize base cases

        # dp[i] = the number of distinct ways to reach step i

        dp[0] = 1 # at step 0 it only has 1 way to reach it by doing nothing
        dp[1] = 1 # at step 1 there is only 1 way to reach it by doing one step
         

        # 3. Build answers using previous results
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # 4. Return final answer
        return dp[n]

