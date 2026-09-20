class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        elif s==t:
            return t

        countT = {}

        window = {}

        for i in t:
            countT[i] = 1 + countT.get(i,0)

        have=0
        need=len(countT)

        l=0
        r=0

        res =[-1,-1]
        resLen = float("infinity")

        while r < len(s):

            i= s[r]
            window[i] = 1 + window.get(i,0)

            if i in countT and window[i]==countT[i]:
                have+=1

            while have==need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1


                window[s[l]]-=1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1

                l+=1

            
            r+=1
        l=res[0]
        r=res[1]

        return s[l:r+1]