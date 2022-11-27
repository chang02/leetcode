from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        idx = len(dp) - 2
        
        while idx >= 0:
            n = nums[idx]
            min = 10000
            for x in range(0, n):
                if idx + x + 1 > len(dp) - 1:
                    break
                if dp[idx+x+1] < min:
                    min = dp[idx+x+1]
            dp[idx] = min + 1
            idx -= 1
        return dp[0]