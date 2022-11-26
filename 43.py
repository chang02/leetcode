from typing import List

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        arr = []
        for idx, num2s in enumerate(reversed(num2)):
            arr.append(self.multiply2(list(num1), num2s, idx))
        resArr = self.add(arr)
        while resArr[0] == "0" and len(resArr) > 1:
            del resArr[0]
        return "".join(resArr)
    
    def multiply2(self, num1: List[str], num2: str, nth: int) -> List[str]:
        res: List[str] = []
        res = res + [0] * nth
        n = 0
        for s in reversed(num1):
            m = int(s) * int(num2) + n
            res.insert(0, str(m % 10))
            n = int(m/10)
        if n != 0:
            res.insert(0, n)
        return res
    
    def add(self, arr: List[List[str]]) -> List[str]:
        res = []
        length = len(arr[-1])
        idx = -1
        n = 0
        while True:
            if (idx * (-1)) > length:
                if n != 0:
                    res.insert(0, str(n))
                break
            sum = 0
            for row in arr:
                num = 0
                try:
                    num = int(row[idx])
                except:
                    num = 0
                sum += num
            sum += n
            res.insert(0, str(sum % 10))
            n = int(sum / 10)
            idx -= 1
        return res