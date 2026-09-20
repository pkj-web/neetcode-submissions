class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = []
        group = {}
        '''
        act
        '''


        for i in strs:
            i.lower()
            #y= "".join(sorted(i))
            x.append(i)
            


        # now we have an array with the elements all lower case and sorted aplhabetically
        for i in x:

            key = "".join(sorted(i)) # act
            if key not in group:
                group[key] = []
            
            group[key].append(i)
            





        return list(group.values())
        