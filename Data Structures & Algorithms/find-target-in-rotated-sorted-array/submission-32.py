class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l=0
        r=len(nums)-1


        while l <= r:


            m = (l+r)//2

            if nums[m]==target:
                return m

            elif nums[l]<=nums[m]:
                if (target < nums[l] or target > nums[m]): # [3,4,5]
                    l=m+1
                else:
                    r=m-1

            else:
                if (target > nums[r] or target < nums[m]): #[6] m [1,2]
                    r=m-1
                else:
                    l=m+1

        return -1
        