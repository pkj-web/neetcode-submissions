class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = []
   


        # pair = [[1,3],[4,2]]

        for p,s in zip(position,speed):
            pair.append((p,s))
            
        pair.sort(reverse=True) # the closest to the target. [[4,2],[1,3]]

        stack = []


        for p,s in pair:
            stack.append((target-p)/s) # time = distance/speed, [2,2]
            while len(stack)>= 2 and stack[-1] <=stack[-2]: #[2]
                stack.pop()


        return len(stack) # 1



        



        # returngint the len haahahahah max v
        