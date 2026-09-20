class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l=0
        r=0
        hashmap = {}
        res=0
        maxF= 0
        while r < len(s):
            i =  s[r]
            hashmap[i] = 1 + hashmap.get(i,0)
            maxF=max(maxF, hashmap[i])
            
            while( ((r-l+1) - maxF) > k):
                hashmap[s[l]]-=1
                l+=1

            
            

            
            res=max(res, (r-l+1))


            r+=1
        return res
        