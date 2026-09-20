

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []  

        for i, t in enumerate(temperatures):
            # Pop from stack while current temp is higher than stacked temp
            while stack and t > stack[-1][1]:
                stacki, stackt = stack.pop()
                res[stacki] = i - stacki  # calculate number of days until warmer temperature
            stack.append((i, t))  # store index first, temp second

        return res


        # [(0,30)], 

