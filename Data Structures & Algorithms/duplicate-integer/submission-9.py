class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # i can brute a O(N^2), but ik there is better 
        # maybe a hashmap approach 

        if ( len(set(nums)) < len(nums)) : 
            return True
        return False

        



        