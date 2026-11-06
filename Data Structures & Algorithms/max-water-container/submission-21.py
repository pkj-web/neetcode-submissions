class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # attempt it bruh



        l=0
        r=len(heights)-1
        maxWater = 0
        while l < r:

            maxWater = max(maxWater, ( (r-l) * min(heights[l], heights[r]) ) )

            if heights[l] < heights[r]:
                l+=1
            elif heights[r] < heights[l]:
                r-=1
            else:
                l+=1
                r-=1
            


        return maxWater


        