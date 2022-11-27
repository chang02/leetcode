class Solution:
    def myPow(self, x: float, n: int) -> float:
        isPositive = n > 0
        if not isPositive:
            n = n * (-1)
        if n == 0: return 1
        if x == 0: return 0
        if x == 1: return 1
        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1
        res = 1
        if isPositive:
            for i in range(0, n):
                res *= x
                if abs(res) < 0.00001:
                    break
            return res
        else:
            for i in range(0, n):
                res /= x
                if abs(res) < 0.00001:
                    break
            return res