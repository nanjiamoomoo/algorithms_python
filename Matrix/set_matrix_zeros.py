"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1



"""
class Solution:
    def set_zeros(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        #step1: find all the 0 position:
        if not matrix:
            return
        
        m = len(matrix)
        n = len(matrix[0])

        xset = set()
        yset = set()

        for x in range(m):
            for y in range(n):
                if not matrix[x][y]:
                    xset.add(x)
                    yset.add(y)
        
        for x in range(m):
            for y in range(n):
                if x in xset or y in yset:
                    matrix[x][y] = 0
        
        #TC: O(m*n)
        #SC: O(m + n)
        """
        Could you devise a constant space solution? 
        
        class Solution:
            def setZeroes(self, matrix: List[List[int]]) -> None:           
                # we use a special value to represents this cells changed state, that is changed to zero due to inline with other zeros.
                for x in range(len(matrix)):
                    for y in range(len(matrix[0])):
                        if matrix[x][y] == 0:
                            for k in range(len(matrix[0])):
                                if matrix[x][k] != 0:
                                    matrix[x][k] = float('-inf') #we use -inf to represents the value that originally not zero, but turned into zero
                            for k in range(len(matrix)):
                                if matrix[k][y] != 0:
                                    matrix[k][y] = float('-inf')
                                    
                for x in range(len(matrix)):
                    for y in range(len(matrix[0])):
                        if matrix[x][y] == float('-inf'):
                            matrix[x][y] = 0
        """
                    