class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)

        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Build the DP array
        for i in range(2, len(nums)):
            # Skip current house OR rob current house
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[-1]