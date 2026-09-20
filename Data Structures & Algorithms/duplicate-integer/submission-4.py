class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        x = len(nums); # 4

        for i in range(0,x): # LOOP THORUHG THE ENTIRE ARRAY
            for j in range(i+1,x): # 2->3
                if nums[i] == nums[j]:
                    return True;

        return False;
            

        