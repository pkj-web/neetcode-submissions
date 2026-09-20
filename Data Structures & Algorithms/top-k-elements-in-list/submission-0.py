class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        count = Counter(nums) # {1:1, 2:2, 3:3}, left is number right is freq of that num

        most_common = count.most_common(k) # [(2,2),(3,3)]


        return [num for num, freq in most_common] # returns [the nums of most_common]
        



    





        