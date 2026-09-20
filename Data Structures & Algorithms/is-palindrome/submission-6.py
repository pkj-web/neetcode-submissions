class Solution:
    def isPalindrome(self, s: str) -> bool:


        # need some sort of loop for the note:
        res = []
        for i in s:
            if i.isalnum():
                res.append(i.lower())
        
        x = "".join(res)
        # x = wasitacaroracatisaw

        
        left = 0

        right = len(x)-1

        while left < right:

            if x[left] != x[right]: # unknown cause of string index out of range in two pointers
                return False
            
            left+=1
            right-=1
        
        return True
        