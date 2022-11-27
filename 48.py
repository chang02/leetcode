from typing import List
import copy

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        c = copy.deepcopy(matrix)
        s = len(matrix)-1
        for i in range(0, s+1):
            for j in range(0, s+1):
                matrix[i][j] = c[s-j][i]
        