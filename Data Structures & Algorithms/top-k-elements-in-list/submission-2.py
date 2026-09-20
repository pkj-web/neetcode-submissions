class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        result = []

        hash_map = Counter(nums)

        most_common = hash_map.most_common(k)


        for pair in most_common:
            key = pair[0]

            result.append(key)

        return result




        