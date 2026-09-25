class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:



        l=0
        r=0
        hashset = set()
        res=0
        while r < len(s):
            
            

            # some kind of if or while condition to remove from hashset with prob a shrink with l+=1    
            while (s[r] in hashset):
                hashset.remove(s[l])
                l+=1

            
            hashset.add(s[r])
            res = max(res, (r-l+1))
            r+=1
        return res

        