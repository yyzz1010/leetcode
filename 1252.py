import numpy as np

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = np.zeros((n, m))
        for i in indices:
            matrix[i[0]] += 1
            matrix[:, i[1]] += 1
        count = 0
        for x in matrix:
            for y in x:
                if y % 2 != 0:
                    count += 1
        return count
