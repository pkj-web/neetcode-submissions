class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0

        right = len(height)-1
        res = 0


        # these twoe are the one timers
        x = height[left]
        y = height[right]

        while left < right:
            # update it in here 
        

            if height[left]<height[right]:
                left+=1
                x = max(x, height[left])
                res += x - height[left]


            else:
                
                right-=1
                y = max(y, height[right])
                res+= y - height[right]


        return res


        