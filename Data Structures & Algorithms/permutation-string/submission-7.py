class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # Create frequency map of s1
        count1 = {}
        for char in s1:
            count1[char] = 1 + count1.get(char, 0)
        
        # Sliding window with FIXED size
        l = 0
        count2 = {}
        
        for r in range(len(s2)):
            # Add character to window
            count2[s2[r]] = 1 + count2.get(s2[r], 0)
            
            # Keep window size = len(s1)
            if r - l + 1 > len(s1):
                count2[s2[l]] -= 1
                if count2[s2[l]] == 0:
                    del count2[s2[l]]
                l += 1
            
            # Compare frequency maps when window is full
            if count1 == count2:
                return True
        
        return False