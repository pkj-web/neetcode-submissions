class MedianFinder:

    def __init__(self):

        self.max_in_minheap = []

        self.min_in_maxheap = []







        

    def addNum(self, num: int) -> None:

        if self.min_in_maxheap and num > self.min_in_maxheap[0]:
            heapq.heappush(self.min_in_maxheap, num)
        # self.min_in_maxheap: we need index 0 to be the smallest element always
        # if its a maxheap then the index 0 must be the largest node so if we have 5 6 7 index 0 must be 7 but we way 5 to be the index 0
        else:
            heapq.heappush(self.max_in_minheap, -1*num)

        
        # rebalacning:
        if len(self.max_in_minheap) > len(self.min_in_maxheap) +1:

            val = -1 * heapq.heappop(self.max_in_minheap)
            heapq.heappush(self.min_in_maxheap, val)

        elif len(self.min_in_maxheap) > len(self.max_in_minheap) + 1:
            val = heapq.heappop(self.min_in_maxheap)
            heapq.heappush(self.max_in_minheap, val*-1)

        


        

    def findMedian(self) -> float:

        if len(self.max_in_minheap) > len( self.min_in_maxheap):
            return -1 * self.max_in_minheap[0]

        elif len(self.min_in_maxheap) > len(self.max_in_minheap):
            return self.min_in_maxheap[0]

        else:
            return ((-1 * self.max_in_minheap[0]) + self.min_in_maxheap[0]) / 2.0
        
        