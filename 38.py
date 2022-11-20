class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            beforeStr: str = self.countAndSay(n-1)
            return self.process(beforeStr)
    
    def process(self, s: str) -> str:
        res = ""
        index = 0
        while True:
            thisNumber, count, nextIndex = self.getThisNumberAndCountAndNextIndex(s, index)
            res += str(count)
            res += thisNumber
            index = nextIndex
            if (nextIndex >= len(s)):
                break
        return res
    
    def getThisNumberAndCountAndNextIndex(self, str: str, i: int) -> (str, int, int):
        thisNumber = str[i]
        count = 0
        index = i
        while index < len(str) and str[index] == thisNumber:
            count += 1
            index += 1
        return (thisNumber, count, index)