from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        imin = 0
        imax = n - 1
        jmin = 0
        jmax = n - 1
        
        res = [[0] * n for _ in range(n)]
        
        i = 0
        j = 0
        state = "right"
        nextObj = {
            "right": "down",
            "down": "left",
            "left": "up",
            "up": "right"
        }
        nn = 1
        while True:
            if i >= imin and i<= imax and j>=jmin and j<=jmax:
                res[i][j] = nn
                nn += 1
                if state == "right":
                    if j + 1 <= jmax:
                        j += 1
                    else:
                        state = nextObj[state]
                        i += 1
                        imin += 1
                elif state == "down":
                    if i + 1 <= imax:
                        i += 1
                    else:
                        state = nextObj[state]
                        j -= 1
                        jmax -= 1
                elif state == "left":
                    if j - 1 >= jmin:
                        j -= 1
                    else:
                        state = nextObj[state]
                        i -= 1
                        imax -= 1
                elif state == "up":
                    if i - 1 >= imin:
                        i -= 1
                    else:
                        state = nextObj[state]
                        j += 1
                        jmin += 1
            else:
                break
        return res