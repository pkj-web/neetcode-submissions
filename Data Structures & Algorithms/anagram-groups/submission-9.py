class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        hashmap = {}


        for i in strs:
            key = ''.join(sorted(i))

            if not hashmap:
                hashmap[key] = [i] # {act : act,}
            elif key not in hashmap:
                hashmap[key] = [i] # {act: act,     opts: pots, tops}

            else:
                hashmap[key].append(i)

        return list(hashmap.values())
