from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        imin = 0
        imax = len(matrix) - 1
        jmin = 0
        jmax = len(matrix[0]) - 1
        
        res = []
        i = 0
        j = 0
        state = "right"
        nextObj = {
            "right": "down",
            "down": "left",
            "left": "up",
            "up": "right"
        }
        while True:
            print(i)
            print(j)
            print("--")
            if i >= imin and i<= imax and j>=jmin and j<=jmax:
                res.append(matrix[i][j])
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