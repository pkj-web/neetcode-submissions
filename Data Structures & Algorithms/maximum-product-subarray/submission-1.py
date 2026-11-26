class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # Initialize the global maximum product
        res = nums[0]

        # Track the maximum and minimum product ending at the current position
        curMin, curMax = 1, 1

        for num in nums:

            # Save the previous maximum product before updating curMax
            tmp = curMax * num

            # Find the new maximum product:
            # 1. Extend the previous maximum (tmp)
            # 2. Extend the previous minimum (negative * negative = positive)
            # 3. Start a new subarray at num
            curMax = max(tmp, num * curMin, num)

            # Find the new minimum product:
            # 1. Previous maximum multiplied by num (tmp)
            # 2. Previous minimum multiplied by num
            # 3. Start a new subarray at num
            curMin = min(tmp, num * curMin, num)

            # Update the global maximum product
            res = max(res, curMax)

        return res