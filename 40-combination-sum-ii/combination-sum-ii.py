class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        
        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion depth
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Prune: if current candidate exceeds remaining, so will all after it (sorted)
                if candidates[i] > remaining:
                    break
                
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], path)
                path.pop()
        
        backtrack(0, target, [])
        return result