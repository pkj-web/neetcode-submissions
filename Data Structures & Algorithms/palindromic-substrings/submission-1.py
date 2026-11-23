class Solution:
    def countSubstrings(self, s: str) -> int:

        dp = []

        for i in range(len(s)):
            row = []

            for j in range(len(s)):
                row.append(False)


            dp.append(row)

        count = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i,len(s)):
                if s[i]==s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j]=True
                    count+=1

        return count       