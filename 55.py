from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp = [0] * len(nums)
        idx = len(nums) - 2
        distance = 0
        while idx > -1:
            if nums[idx] == 0 and distance == 0:
                distance += 1
            elif nums[idx] <= distance:
                distance += 1
            else:
                distance = 0
            idx -= 1
        return distance == 0