from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # Start from the last digit
        for i in range(len(digits) - 1, -1, -1):

            # If the digit is less than 9, add 1
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # If the digit is 9, change it to 0
            digits[i] = 0

        # When all digits are 9, such as [9] or [9, 9]
        return [1] + digits