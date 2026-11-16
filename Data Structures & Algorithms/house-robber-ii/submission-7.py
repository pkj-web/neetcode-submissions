class Solution:
    def rob(self, nums: List[int]) -> int:

        

        def rob_linear(nums):

            if len(nums)==1:
                return nums[0]

            n=len(nums)
            dp = [0] * n

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            
            for i in range(2, n):

                dp[i] = max(nums[i] + dp[i-2], dp[i-1])

            return dp[-1]

        if len(nums)==1:
                return nums[0]
        s1 = rob_linear(nums[:-1])
        s2 = rob_linear(nums[1:])
        print(s1)
        print(s2)
        
        return max(s1, s2)