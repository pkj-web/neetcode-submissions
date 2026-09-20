class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        hashmap = {}


        # hashmap = {act: [act,] , }
        for s in strs:

            key = "".join(sorted(s))

            if key not in hashmap:

                hashmap[key] =  []

            
            hashmap[key].append(s)

        return list(hashmap.values())
        