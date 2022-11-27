from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        obj = {
            "res": [],
            "remain": nums
        }
        objRes = [obj]
        while True:
            if len(objRes[0]["remain"]) == 0:
                break
            poped = objRes.pop(0)
            for remain in poped["remain"]:
                popedRes: List[int] = poped["res"].copy()
                popedRemain: List[int] = poped["remain"].copy()
                popedRes.append(remain)
                popedRemain.remove(remain)
                objRes.append({
                    "res": popedRes,
                    "remain": popedRemain
                })
        
        return list(map(lambda x:x["res"], objRes))