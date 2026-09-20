class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp  = {}
        l = 0

        res =0

        maxFreq=0

        for r in range(len(s)):

            #get the count of the lettters
            mp[s[r]] = mp.get(s[r],0) + 1


            #  maxfreq
            
            maxFreq = max(maxFreq, mp[s[r]])
            #size = 0


            # invlaoid window size 
            while ((r-l+1) - maxFreq > k):
                mp[s[l]] -=1
                l+=1


            res = max(res, r-l+1)
        return res
        