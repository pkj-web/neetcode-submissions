class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        count = {}


        for n in nums:

            count[n] = 1 + count.get(n,0)


        res = sorted(count, key=lambda x: count[x], reverse=True)

        return res[:k]
        