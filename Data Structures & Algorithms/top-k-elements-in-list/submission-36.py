class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqArray = []

        hashmap = {}


        for i in range(len(nums)+1):
            freqArray.append([])
        

        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)


        for i,j in hashmap.items():
            freqArray[j].append(i)


        array =[]

        for i in range(len(freqArray)-1,0,-1):
            for j in freqArray[i]:
                array.append(j)

                if len(array)==k:
                    return array
        