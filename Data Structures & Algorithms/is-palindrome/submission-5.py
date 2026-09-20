class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s)-1

        x  = []

        for i in s:
            if i.isalnum():
                x.append(i.lower())
        


        pizza = "".join(x)
        right = len(pizza)-1
        while left < right:
            if x[left] != x[right]:
                return False
            left+=1
            right-=1

        return True
        
        