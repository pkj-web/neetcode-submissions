class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        count = Counter(nums) # {1:1, 2:2, 3:3}, left is number right is freq of that num

        most_common = count.most_common(k) # [(2,2),(3,3)]


        for pair in most_common:
            key = pair[0]

            result.append(key)

        return result

        



    





        