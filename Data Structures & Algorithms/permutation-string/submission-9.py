class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = {}

        for i in s1:
            count1[i] = 1 + count1.get(i,0)

        l=0
        r=0
        count2 = {}
        while r < len(s2):
            count2[s2[r]] = 1 + count2.get(s2[r], 0)

            if (r-l+1) > len(s1):
                count2[s2[l]]-=1
                if count2[s2[l]]==0:
                    del count2[s2[l]]
                l+=1

            

            if count1==count2:
                return True
            
            r+=1

        return False



            
        