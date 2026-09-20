class Solution:
    def isPalindrome(self, s: str) -> bool:

        res = []

        for ch in s:
            if(ch.isalnum()):
                res.append(ch.lower())

        
        x = "".join(res)


        left = 0
        right = len(x)-1

        while left < right:

            if(x[left] != x[right]):
                return False

            left+=1
            right-=1


        return True

        