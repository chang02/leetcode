class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = [[] for i in range(numRows)]
        flag = False
        i = 0
        j = 0
        for c in s:
            if flag == False:
                res[i].append(c)
                if i == numRows - 1:
                    i -= 1
                    flag = True
                else:
                    i += 1
            else:
                res[i].append(c)
                if i == 0:
                    i += 1
                    flag = False
                else:
                    i -= 1
        return ''.join(list(map(lambda x: ''.join(x), res)))
            