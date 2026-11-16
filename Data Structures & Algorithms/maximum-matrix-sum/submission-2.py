class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negcount = 0
        minneg = float('inf')
        res = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                res += abs(matrix[i][j])
                if matrix[i][j] < 0:
                    negcount += 1
                minneg = min(minneg, abs(matrix[i][j]))


        if negcount>0 and negcount % 2 != 0:
            res -= (minneg * 2)

        return res


