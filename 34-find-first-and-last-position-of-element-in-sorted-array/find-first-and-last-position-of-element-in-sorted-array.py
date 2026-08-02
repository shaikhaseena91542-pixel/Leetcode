class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findBound(isFirst: bool) -> int:
            lo, hi = 0, len(nums) - 1
            result = -1

            while lo <= hi:
                mid = (lo + hi) // 2

                if nums[mid] == target:
                    result = mid
                    if isFirst:
                        hi = mid - 1  # keep searching left
                    else:
                        lo = mid + 1  # keep searching right
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1

            return result

        first = findBound(True)
        if first == -1:
            return [-1, -1]

        last = findBound(False)
        return [first, last]