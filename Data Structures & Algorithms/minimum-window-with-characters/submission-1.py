class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "":
            return ""
        res = [-1,-1]
        resLen = float("infinity")

        counT ={}
        window = {}

        for i in t:
            counT[i] = counT.get(i,0) +1

        have = 0
        need = len(counT)

        l=0

        for r in range(len(s)):

            window[s[r]] = window.get(s[r],0) +1

            if(s[r] in counT and window[s[r]]==counT[s[r]]):
                have +=1

            while have == need:

                if (r-l+1) < resLen:
                    res=[l,r]
                    resLen = (r-l+1)

                
                window[s[l]]-=1
                if(s[l] in counT and window[s[l]] < counT[s[l]]):
                    have-=1

                l+=1

        l, r = res

        if resLen < float("infinity"):
            return s[l: r+1]

        else:
            return ""
