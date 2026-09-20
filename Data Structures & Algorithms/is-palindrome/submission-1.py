class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_char = []

        for ch in s:
            if(ch.isalnum()):
                cleaned_char.append(ch.lower())

        cleaned = "".join(cleaned_char)

        left = 0
        right = len(cleaned)-1

        while left < right:
            if(cleaned[left]!=cleaned[right]):
                return False
            left+=1
            right-=1

        return True
        