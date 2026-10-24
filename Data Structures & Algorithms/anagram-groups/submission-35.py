class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        defaultdictlist = defaultdict(list)

        for i in strs:
            charFreq = [0] * 26
            for j in i:
                charFreq[ord(j)-ord("a")]+=1

            defaultdictlist[tuple(charFreq)].append(i)

        return list(defaultdictlist.values())
        