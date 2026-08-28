from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(start: int, remaining: int, path: List[int]):
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break  # no point trying larger numbers
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i], path)  # i, not i+1 (reuse allowed)
                path.pop()

        backtrack(0, target, [])
        return result