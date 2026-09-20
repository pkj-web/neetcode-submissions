class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height)-1


        x = height[left]

        y = height[right]

        res = 0

        while left < right:

            if height[left]<height[right]:
                left +=1
                x = max(x, height[left])
                res += x - height[left]

            else:
                right -=1
                y = max(y, height[right])
                res += y - height[right]

        return res



        