from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        obj = {
            "res": [],
            "remain": nums
        }
        objRes = [obj]
        s = set()
        while True:
            if len(objRes[0]["remain"]) == 0:
                break
            poped = objRes.pop(0)
            for remain in poped["remain"]:
                popedRes: List[int] = poped["res"].copy()
                popedRemain: List[int] = poped["remain"].copy()
                popedRes.append(remain)
                popedRemain.remove(remain)
                if tuple(popedRes) in s:
                    continue
                else:
                    newObj = {
                        "res": popedRes,
                        "remain": popedRemain
                    }
                    objRes.append(newObj)
                    s.add(tuple(popedRes))
                
        
        return list(map(lambda x:x["res"], objRes))

s = Solution()
print(s.permuteUnique([1,1,2]))