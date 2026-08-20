class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # base for length calculation
        max_len = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:  # ch == ')'
                stack.pop()
                if not stack:
                    stack.append(i)  # new base for future substrings
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len