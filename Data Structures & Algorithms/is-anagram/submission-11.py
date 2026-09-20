class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        string_1 = sorted(s); # ajr
        string_2 = sorted(t); # ajm

        if (string_1 == string_2):
            return True;
        else:
            return False;


