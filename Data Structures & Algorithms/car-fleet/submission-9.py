class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        pair = []

        for p,s in zip(position,speed):
            pair.append((p,s))

        pair.sort(reverse=True)

        # pair = [(4,2), (1,3)]
        stack = []


        for p,s in pair:
            stack.append((target-p)/s) # stack  = [2,2.5]
            if((len(stack)>=2) and stack[-2] >= stack[-1]):
                stack.pop()

            



        return len(stack)
        