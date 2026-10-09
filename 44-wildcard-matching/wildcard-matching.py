class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # dp[j] = does s[:i] match p[:j]
        dp = [False] * (n + 1)
        dp[0] = True

        # empty string vs pattern: only leading '*' can match empty
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[j] = dp[j - 1]
            else:
                break

        for i in range(1, m + 1):
            prev_diag = dp[0]      # dp[i-1][j-1]
            dp[0] = False          # non-empty s can't match empty p
            for j in range(1, n + 1):
                temp = dp[j]       # dp[i-1][j], needed as next diagonal
                if p[j - 1] == '*':
                    # '*' matches empty (dp[j-1]) or one more char (dp[j])
                    dp[j] = dp[j - 1] or dp[j]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[j] = prev_diag
                else:
                    dp[j] = False
                prev_diag = temp

        return dp[n]