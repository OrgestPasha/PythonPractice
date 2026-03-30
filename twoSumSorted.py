from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            tempSum = numbers[left] + numbers[right]
            if target == tempSum:
                return [numbers[left], numbers[right]]
            elif target < tempSum:
                right -= 1
            else:
                left += 1
