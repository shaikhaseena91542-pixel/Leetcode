class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (but not 0 itself) can't be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10

        # For even digit count: x == reverted
        # For odd digit count: x == reverted // 10 (drop the middle digit)
        return x == reverted or x == reverted // 10
        