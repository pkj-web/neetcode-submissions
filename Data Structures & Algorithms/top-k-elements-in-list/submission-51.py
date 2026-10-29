class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # thinking hashmap for counting idk

        hashmap = {}

        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)

        # hashmap = {
        # number : amount
        # 1: 1
        # 2: 2
        # 3: 3
        #}


        # what do do with this hashmap info
        heap = []

        for i,j in hashmap.items():
            heapq.heappush(heap, (j,i))

            if len(heap) > k:
                heapq.heappop(heap)

        # minheap = []
        # minheap = [1]
        # minheap = [1,2]
        # minheap [2,2]
        # minheap [2,3]
        # minheap [3,3]
        # minheap [3,3] so not our answer of [2,3] 

        res = []

        for i,j in heap:
            res.append(j)        

        return res