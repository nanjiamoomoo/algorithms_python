"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        
        n = len(matrix)
        top, bottom, left, right = 0, n - 1, 0, n - 1

        while top <= bottom:
            for x in range(left, right):
                displacement = x - left
                tmp = matrix[top][x]
                matrix[top][x] = matrix[bottom - displacement][left]
                matrix[bottom - displacement][left] = matrix[bottom][right - displacement]
                matrix[bottom][right - displacement] = matrix[top + displacement][right]
                matrix[top + displacement][right] = tmp
            top += 1
            bottom -= 1
            right -= 1
            left += 1
        return
    
    """
        another method:
        first transpose:
        then do row reverse

        if not matrix:
            return
        n = len(matrix)
        def transpose(matrix:list[list]) -> None:
            for x in range(n):
                for y in range(x, n):
                    matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
        def reverserows(matrix:list[list])-> None:
            for x in range(n):
                left, right = 0, n - 1
                while left < right:
                    matrix[x][left], matrix[x][right] = matrix[x][right], matrix[x][left]
                    left += 1
                    right -= 1
        transpose(matrix)
        reverserows(matrix)
                
    """