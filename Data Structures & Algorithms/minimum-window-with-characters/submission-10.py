class Solution:
    def minWindow(self, s: str, t: str) -> str:

        hashmapT = {}

        for i in t:
            hashmapT[i] = 1 + hashmapT.get(i,0)
        

        have=0
        need=len(hashmapT)

        l=0
        r=0

        res = [-1,-1]

        resLen=float("infinity")
        hashmap = {}
        while r < len(s):


            hashmap[s[r]] = 1 + hashmap.get(s[r],0)

            if s[r] in hashmapT and hashmap[s[r]]==hashmapT[s[r]]:
                have+=1

            while have == need:

                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = (r-l+1)

                hashmap[s[l]]-=1

                if s[l] in hashmapT and hashmapT[s[l]] > hashmap[s[l]] :
                    have-=1


                l+=1
            r+=1


        l=res[0]
        r=res[1]
        return s[l:r+1]
        