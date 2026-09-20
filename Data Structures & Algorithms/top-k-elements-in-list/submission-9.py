class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for i in nums:
            count[i] = 1 + count.get(i,0)


        res= sorted(count, reverse=True, key=lambda x: count[x])

        return res[:k]
        