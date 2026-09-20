class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashset=set(nums)

        longest =0
        for i in hashset:
            if not (i-1) in hashset:
                length=1

                while (i+length) in hashset:
                    length+=1

                longest =max(length, longest)


        return longest
        