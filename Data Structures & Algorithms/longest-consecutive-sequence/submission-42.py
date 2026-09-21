class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        x = set(nums)

        y = 0
        for i in x:
            if (i-1) not in x:
                length=1

                while (i+length) in x:
                    length+=1

                y= max(y,length)
        return y
        