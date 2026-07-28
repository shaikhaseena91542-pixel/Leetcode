class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ""

        start, max_len = 0, 1

        def expand_around_center(left: int, right: int) -> int:
            # Expand outward while characters match, then return the
            # length of the palindrome found (one step past the bounds).
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            len1 = expand_around_center(i, i)       # odd-length, e.g. "aba"
            len2 = expand_around_center(i, i + 1)    # even-length, e.g. "abba"
            curr_len = max(len1, len2)

            if curr_len > max_len:
                max_len = curr_len
                start = i - (curr_len - 1) // 2

        return s[start:start + max_len]


# Quick test
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))  # "bab" (or "aba", both valid)
    print(sol.longestPalindrome("cbbd"))   # "bb"