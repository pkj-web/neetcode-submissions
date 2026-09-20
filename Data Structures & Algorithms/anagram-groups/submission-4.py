class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for n in strs:

            x = "".join(sorted(n))

            if(x not in hashmap):
                hashmap[x] = []

            hashmap[x].append(n)

        return list(hashmap.values())