class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:


        # arr aka nums in non decreasing order
        # retuen an array of the squares of each number thne sort



        arr = []

        l=0

        r=len(nums)-1



        while l <= r:
            

            if nums[l] <= nums[r]:
                arr.append(nums[l] ** 2)
                l+=1
            '''
            elif nums[r] > nums[l]:

                arr.append(nums[r]**2)
                r-=1
            else:

                l+=1

                r-=1
            '''
        return sorted(arr)
        