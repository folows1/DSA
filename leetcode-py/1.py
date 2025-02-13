from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        passed = {}

        for idx, num in enumerate(nums):
            if passed.get(target - num) is not None:
                return [passed[target - num], idx]
            passed[num] = idx

        return []
