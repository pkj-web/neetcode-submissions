class Solution:
    def maxProduct(self, nums: List[int]) -> int:


        res = nums[0]

        curmax = 1
        curmin = 1

        for i in nums:

            tmp1 = i * curmax

            tmp2 = i * curmin

            curmax = max(tmp1, tmp2, i)

            curmin = min(tmp1, tmp2, i)

            res=max(res,curmax)

        return res
        