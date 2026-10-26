class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap = []
        hashmap = {}

        for i in nums:
             hashmap[i] = 1 + hashmap.get(i,0)

        for i,j in hashmap.items():
            
            
            heapq.heappush(heap, (j,i))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        for i, j in heap:
            res.append(j)

        return res

        '''

        lets just defualt to a min heap so the top of the heap is the smallest num:
        heap[1,2,3,56]
        if so pop it would be the 1 right?
        asnwer: yes BRO

        '''