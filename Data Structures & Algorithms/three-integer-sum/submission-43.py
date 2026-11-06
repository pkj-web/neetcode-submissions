class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        nums.sort() # -4, -1,-1,0,1,2
        res=[]
        for i,j in enumerate(nums):
            
            if j > 0: # postive check
                break

            elif i > 0 and j == nums[i-1]:   
                continue # 	Skip duplicate starting numbers fir tge outer loop in the example both sub arryas starting we -1 were found in the same iteration, however th enext iteration cant start with the -1 any more due to the outer loop going to a new iteration

            

            l= i + 1 # searach asfter i

            r = len(nums) - 1

        
            while l < r:

                threeSum = nums[r] + nums[i] + nums[l]


                if threeSum < 0:
                    l+=1

                elif threeSum > 0:
                    r-=1

                else:

                    res.append([nums[r], nums[i], nums[l]])
                    l+=1
                    r-=1

                    while l < r and nums[l]==nums[l-1]: # duplicate-skipping logic for your left pointer
                        l+=1

        return res