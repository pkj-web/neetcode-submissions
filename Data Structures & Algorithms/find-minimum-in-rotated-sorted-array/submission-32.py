class Solution:
    def findMin(self, nums: List[int]) -> int:

        l=0
        r=len(nums)-1

        '''
        Input: nums = [3,4,5,6,1,2]
        Output: 1

        iteration #1: 
        l=0
        r=5
        mid = 2


        '''
        while l < r:
            mid = (l+r) // 2

            if nums[mid] > nums[r]: # 5 > 2: this tells us the min or rotation point is after mid
                l = mid + 1

            else:
                r = mid 


        
        return nums[l]
        