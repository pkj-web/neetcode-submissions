
class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        # Build a 2D DP array initialized to False
        # dp[i][j] = True if the substring from index i to j is a palindrome
        dp = []
        for i in range(n):
            row = []

            for j in range(n):
                row.append(False)

            dp.append(row)

        # Track the starting index and length of the longest palindrome
        resIdx = 0
        resLen = 0

        # i represents the starting index (rows)
        # Iterate backwards so dp[i+1][j-1] is already calculated
        for i in range(n - 1, -1, -1):

            # j represents the ending index (columns)
            # Start at i and move forward, expanding the substring to the right
            for j in range(i, n):

                # The outer characters must match
                # If the substring length is <= 3, it's automatically a palindrome
                # Otherwise, the inner substring must already be a palindrome
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):

                    # Mark this substring as a palindrome
                    dp[i][j] = True

                    # If this palindrome is longer than our current best, update it
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1

        # Return the longest palindrome using its starting index and length
        return s[resIdx : resIdx + resLen]
