class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        # [1,2,4,6]
        # [48,24,12,8]


        x = []
      
     
        y = math.prod(nums)
        
        for i in range(len(nums)):

            if(nums[i]<0):
                x.append(y//nums[i])
            elif(nums[i]!=0):
                x.append(y//nums[i])
            else:
                z = nums[:i] + nums[i+1:]
                gg = math.prod(z)
                x.append(gg//1)

        return (x)

            