from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for st in strs:
            k = tuple(self.strToBitArr(st))
            if k in a:
                a[k].append(st)
            else:
                a[k] = [st]
        return list(a.values())
        
    def strToBitArr(self, s: str) -> List[int]:
        res = [0] * 26
        for c in s:
            res[ord(c) - ord("a")] += 1
        return res
        