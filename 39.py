from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        tempArrays: List[List[int]] = []
        res: List[List[int]] = []

        for candidate in candidates:
            if candidate == target:
                res.append([candidate])
            elif candidate < target:
                tempArrays.append([candidate])
        
        while True:
            if (len(tempArrays) == 0): break
            poped = tempArrays.pop(0)
            sumOfPoped = sum(poped)
            if sumOfPoped == target:
                res.append(poped)
            elif sumOfPoped < target:
                for candidate in candidates:
                    if poped[-1] <= candidate and sumOfPoped + candidate <= target:
                        tempArrays.append(poped + [candidate])
        return res
