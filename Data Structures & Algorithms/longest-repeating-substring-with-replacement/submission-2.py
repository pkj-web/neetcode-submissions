class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res =0

        maxFreq = 0

        l =0
        mp = {}

        for r in range(len(s)):

            mp[s[r]] = mp.get(s[r], 0) + 1

            maxFreq = max(maxFreq, mp[s[r]])

            if ((r-l+1)-maxFreq > k):
                mp[s[l]]-=1
                l+=1

            res = max(res, r-l+1)


        return res

