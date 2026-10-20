class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        defaultdictlist = defaultdict(list) # group think defaultdict maybe


        for i in strs: # for each word
            letters = [0] * 26
            for j in i: # for each letter in each word
                letters[ord(j) -  ord("a")] +=1 # unsure of syntax here

            
            defaultdictlist[tuple(letters)].append(i)

        return list(defaultdictlist.values())




        """
        letters = [0,0,0,0,0,0..........]
        """
        