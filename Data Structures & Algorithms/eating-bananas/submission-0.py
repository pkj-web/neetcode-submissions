class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ##### Input: piles = [1,4,3,2], h = 9

        #     Output: 2
        ##### total bananas: 10 bananas and 9 hours to eat them all
        #####

        left = 1

        right = max(piles) # 4

        res = right
        while left <= right:

            mid = (left+right)//2 # 1

            totalTime = 0
            for i in piles:
                totalTime += math.ceil(i/mid)
            
            if totalTime <= h:
                res = mid
                right = mid -1

            else:
                left = mid +1

        return res






           
        