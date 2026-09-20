class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashset = set(nums) #[2,20,4,10,3,5]

        longest = 0

        for i in hashset:

        

            if(i-1) not in hashset:

                length=1

                while (i+length) in hashset:
                    length+=1
                
                longest = max(longest,length)

        return longest

            
        