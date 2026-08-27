class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for _ in range(n - 1):
            next_result = []
            i = 0
            while i < len(result):
                digit = result[i]
                count = 1
                while i + 1 < len(result) and result[i + 1] == digit:
                    i += 1
                    count += 1
                next_result.append(str(count))
                next_result.append(digit)
                i += 1
            result = "".join(next_result)

        return result