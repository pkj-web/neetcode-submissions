class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # nums = [2,20,4,10,3,4,5]

        # 4
        if not nums: # if not is the empty or like null checker
            return 0
        x = sorted(nums)
        max_streak = 0
        current_streak = 0
        # [2,3,4,4,5,10,20]
        for i in range(len(x)-1):
         
            if(x[i]+1 ==  x[i+1]):
                current_streak= current_streak + 1
            elif(x[i]==x[i+1]):
                continue
            else:
                current_streak = 0

            max_streak = max(max_streak, current_streak)

        return max_streak+1





        