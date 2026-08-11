class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Find the length of the longest sequential prefix
        prefix_sum = nums[0]
        i = 1
        while i < n and nums[i] == nums[i - 1] + 1:
            prefix_sum += nums[i]
            i += 1
        
        # Find the smallest integer >= prefix_sum that is missing from nums
        num_set = set(nums)
        x = prefix_sum
        while x in num_set:
            x += 1
        
        return x