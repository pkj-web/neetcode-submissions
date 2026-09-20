class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        

        # group = [act:["act"], opts["pots"] ]
        group = {}

        #  opts

        for key in strs:
            x = "".join(sorted(key))
            if x not in group:
                group[x] = []
            

            group[x].append(key)

        
        return list(group.values())

            



        