from functools import lru_cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = total stones from piles[i] to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dp(i, M):
            # If we can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            # Try taking X piles, where 1 <= X <= 2M
            for X in range(1, 2 * M + 1):
                opponent = dp(i + X, max(M, X))

                # Alice gets remaining stones minus
                # the maximum stones opponent can get
                current = suffix[i] - opponent

                best = max(best, current)

            return best

        return dp(0, 1)