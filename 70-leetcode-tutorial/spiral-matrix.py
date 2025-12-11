# Given an m x n matrix, return all elements of the matrix in spiral order.
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ret = []
        while matrix:
            #1. add first row/list of matrix:
            ret += (matrix.pop(0))
            #2. append last element all list in orders
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            #3. add reverse of last row/list
            if matrix:
                ret += (matrix.pop()[::-1])
            #4. append first element of all rows/lists in reverse
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret

if __name__ == "__main__":

    solution = Solution()
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    res = solution.spiralOrder(matrix)
    print(res)

    ## 1 2 3 4
    ## 5 6 7 8
    ## 9 10 11 12