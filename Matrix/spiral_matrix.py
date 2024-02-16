"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
class Solution:
    def sprial_print(self, matrix:list[list[int]]) -> list:
        if not matrix:
            return matrix
        
        m, n= len(matrix), len(matrix[0])
        top, right, bottom, left = 0, n - 1, m - 1, 0

        res = []
        while len(res) < m * n:
            for x in range(left, right + 1): #print top
                res.append(matrix[top][x])
            top += 1
            for x in range(top, bottom + 1): # print right
                res.append(matrix[x][right])
            right -= 1
            if top <= bottom: # print bottom, this check to make sure there is still bottom element to print
                for x in range(right, left - 1, -1):
                    res.append(matrix[bottom][x])
                bottom -= 1
            if left <= right: #print left, this check to make sure there is still left element to print
                for x in range(bottom, top - 1, -1):
                    res.append(matrix[x][left])
                left += 1

        return res
            

if __name__=="__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    sol = Solution()
    res = sol.sprial_print(matrix)
    print(res)