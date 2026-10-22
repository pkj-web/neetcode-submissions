class MedianFinder:

    '''
    [ -2 -1 | 3 ]
    '''

    def __init__(self):

        self.max_in_minheap = [] # 1st half
        self.min_in_maxheap = [] # 2nd second
        

    def addNum(self, num: int) -> None:

        if self.min_in_maxheap and num > self.min_in_maxheap[0]:
            heapq.heappush(self.min_in_maxheap, num)

        else:
            heapq.heappush(self.max_in_minheap, -1 * num)


        if len(self.max_in_minheap) > len(self.min_in_maxheap)+ 1:
            val = -1 * heapq.heappop(self.max_in_minheap)
            heapq.heappush(self.min_in_maxheap, val)

        elif len(self.min_in_maxheap) > len(self.max_in_minheap) + 1:
            val = heapq.heappop(self.min_in_maxheap)
            heapq.heappush(self.max_in_minheap, val * -1)



    def findMedian(self) -> float:

        if len(self.max_in_minheap) > len(self.min_in_maxheap):
            return self.max_in_minheap[0] * -1

        elif len(self.min_in_maxheap) > len(self.max_in_minheap):
            return self.min_in_maxheap[0]

        
        return ( (-1 * self.max_in_minheap[0]) + self.min_in_maxheap[0])  / 2.0

        
        