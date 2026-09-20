class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        string_one = sorted(s)
        string_two = sorted(t)

        if string_one == string_two:
            return True
        else:
            return False
        