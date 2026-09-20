class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_char = []

        for ch in s:
            if ch.isalnum():
                cleaned_char.append(ch.lower())
        
        x = "".join(cleaned_char) # "wasitacaroracatisaw"


        left = 0

        right = len(x)-1

        while left < right:

            if(x[left]!= x[right]):
                return False
            
            left+=1
            right-=1
        
        return True



            
        



        