from typing import List
import sys

# 카데인 알고리즘
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = []
        for idx, num in enumerate(nums):
            if idx == 0:
                res.append(num)
            else:
                res.append(max(res[-1] + num, num))
        return max(res)