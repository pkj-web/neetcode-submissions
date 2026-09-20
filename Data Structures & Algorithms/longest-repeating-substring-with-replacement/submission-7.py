class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        l=0
        r=0


        res = 0
        maxF = 0

        hashmap= {}

        while r < len(s):

            i = s[r]

            hashmap[i] = 1 + hashmap.get(i,0)
            maxF = max(hashmap[i],maxF)
            if ((r-l+1) - maxF > k):
                hashmap[s[l]]-=1
                l+=1

            res = max((r-l+1),res)
            # return len of the max window size???? idk maybe
            r+=1
        return res


        