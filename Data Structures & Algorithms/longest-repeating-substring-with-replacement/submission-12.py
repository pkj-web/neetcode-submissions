class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        l=0
        r=0
        maxLetterLen = 0
        hashmap = {}
        res = 0
        while r < len(s):
            hashmap[s[r]] = 1 + hashmap.get(s[r],0)
            maxLetterLen = max(maxLetterLen, hashmap[s[r]])

            if ((r-l+1) - maxLetterLen > k):
                hashmap[s[l]]-=1
                l+=1


            res = max(res, (r-l+1))
            r+=1
        return res

        