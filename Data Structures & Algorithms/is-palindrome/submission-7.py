class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        res = []

        for i in s:
            if(i.isalnum()):
                res.append(i.lower())

        y = "".join(res)

        left = 0
        right = len(y)-1

    

        while left < right:

            if y[left]!=y[right]:
                return False

            left+=1
            right-=1

        return True
