class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        result = []

        def backtrack(index, path):
            if index == len(digits):
                result.append(''.join(path))
                return
            for letter in phone[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return result


# Test it
if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations("23"))
    # ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    print(sol.letterCombinations("2"))
    # ["a","b","c"]

    print(sol.letterCombinations(""))
    # []