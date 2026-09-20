class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = sorted(s) # a a c c e r r
        y = sorted(t) # a a c c e r r
        if(x==y):
            return True

        else:
            return False
        