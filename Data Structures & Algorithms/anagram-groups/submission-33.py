class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # pretty muhc hashmap assining as we move thorugh the array

        defaultdictlist = defaultdict(list) # group think defaultdict for hashmap with creates key auto when needed


        for i in strs: # for each word
            letters = [0] * 26 # freq array for each letter
            for j in i: # for each letter in each word
                letters[ord(j) -  ord("a")] +=1 # unsure of syntax here

            
            defaultdictlist[tuple(letters)].append(i)

        return list(defaultdictlist.values())




        """
        letters = [0,0,0,0,0,0..........]
        """
        