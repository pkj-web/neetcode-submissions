class Solution:
    def findMin(self, nums: List[int]) -> int:

        # all we are doing this returing the mimnum element of the array so lets think and cook :)

        l=0
        r=len(nums)-1

        while l < r:

            mid = (l+r)//2


            if (nums[mid] > nums[r]):
                l= mid+1

            else:
                r=mid

        return nums[r]



        