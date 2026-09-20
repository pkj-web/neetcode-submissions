class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1 # 0 7
        res = 0

        while l < r: # 0 < 7
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]: # 1 <= 7, 7<=6
                l += 1
            else:
                r -= 1
        return res