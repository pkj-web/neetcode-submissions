class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # lock pk 200k entry ?
        # then lock in twin




        l=0

        r=len(nums)-1

        while l <= r: # maybe a change here

            mid = (l+r) // 2

            if nums[mid]==target:
                return mid

            elif ( nums[mid] > target):
                r= mid -1

            else:
                l = mid + 1

        
        return r+1