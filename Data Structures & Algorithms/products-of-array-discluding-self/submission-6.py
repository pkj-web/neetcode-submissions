class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        res = [1] * len(nums)

        prefix = 1


        # res = [1,1,1,1]
        for i in range(len(res)):
            res[i] = prefix
            prefix *= nums[i]

        suffix=1 #aka postfix

        for i in range(len(res)-1,-1,-1): # right to left set up with the -1's.
            res[i] *= suffix
            suffix *= nums[i]

        return res
        