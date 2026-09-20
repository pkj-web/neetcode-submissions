class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        array = []

        nums.sort()


        for i,j in enumerate(nums):
            if j > 0:
                break

            elif i > 0 and j==nums[i-1]:
                continue
            

            l=i+1
            r=len(nums)-1

            while l < r:
                threeSum = j + nums[l] + nums[r]

                if threeSum < 0:
                    l+=1
                elif threeSum > 0:
                    r-=1
                else:
                    array.append([j, nums[l], nums[r]])
                    l+=1
                    r-=1

                    while l < r and nums[l]==nums[l-1]:
                        l+=1
        return array
