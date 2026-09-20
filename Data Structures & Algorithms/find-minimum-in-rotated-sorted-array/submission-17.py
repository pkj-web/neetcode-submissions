class Solution:
    def findMin(self, nums: List[int]) -> int:

       start = 0


       end = len(nums)-1

       nums.sort()

       return nums[0] 
        