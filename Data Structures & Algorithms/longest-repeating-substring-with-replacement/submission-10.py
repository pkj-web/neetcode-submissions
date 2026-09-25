class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        longest = 0

        l=0
        r=0


        maxF=0

        hashmap = {}
        while r < len(s):
            hashmap[s[r]] = 1 + hashmap.get(s[r],0)
            

            
            maxF=max(maxF,hashmap[s[r]])

            if ((r-l+1) - maxF > k):
                hashmap[s[l]]-=1
                l+=1
            longest=max(longest,(r-l+1))
            r+=1
        

        return longest

        