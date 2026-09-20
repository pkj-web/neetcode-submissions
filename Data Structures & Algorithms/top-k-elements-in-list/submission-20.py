class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for n in nums:
            count[n] = count.get(n,0) + 1 # formulate a frequency map


        #sort the thing freq map

        res = sorted(count, reverse = True, key=lambda x: count[x])

        return res[:k]
        