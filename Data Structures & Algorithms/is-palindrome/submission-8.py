class Solution:
    def isPalindrome(self, s: str) -> bool:


        array = []


        for i in s:
            if i.isalnum():
                array.append(i.lower())

        x = "".join(array)

        left = 0
        right = len(x)-1

        while left < right:
            if(x[left] != x[right]):
                return False
            
            left+=1
            right-=1
        

        return True
        