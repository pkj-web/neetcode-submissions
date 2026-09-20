class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        res = [-1,-1]


        resLen = float("infinity")



        have = 0


        countT = {}

        for i in t:
            countT[i] = 1 + countT.get(i,0)

        need = len(countT)

        
        
        
        hashmap = {}
        l=0
        r=0

        while r < len(s):

            i= s[r]

            hashmap[i] = 1+hashmap.get(i,0)

            if i in countT and hashmap[i]==countT[i]:
                have+=1

            while have == need:

                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = (r-l+1)

                hashmap[s[l]]-=1

                if s[l] in countT and hashmap[s[l]] < countT[s[l]]:
                    have-=1
                l+=1

            r+=1
        l = res[0]
        r = res[1]

        return s[l: r+1]

        