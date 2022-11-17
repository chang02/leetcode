class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False] * n for i in range(0, n)]
        res = ""
        
        for j in range(n):
            for i in range(j+1):
                if s[i] == s[j]:
                    if j - i < 2:
                        dp[i][j] = True
                    elif dp[i+1][j-1] == True:
                        dp[i][j] = True
                if dp[i][j]:
                    if len(s[i:j+1]) > len(res):
                        res = s[i:j+1]
        return res
