class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashset = set(nums) # {1,2,3}, len = 3 in example 1
                            # {1,2,3,4}, len= 4 in example 2

        if len(hashset) < len(nums):
            return True
        else:
            return False

            

            
    
        