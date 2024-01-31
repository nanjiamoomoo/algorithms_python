# Max Water Trapped II
"""
Given a non-negative integer 2D array representing the heights of bars in a matrix. Suppose each bar has length and width of 1. 
Find the largest amount of water that can be trapped in the matrix. The water can flow into a neighboring bar if the neighboring bar's height 
is smaller than the water's height. Each bar has 4 neighboring bars to the left, right, up and down side.

Assumptions
The given matrix is not null and has size of M * N, where M > 0 and N > 0, all the values are non-negative integers in the matrix.
Examples

{ { 2, 3, 4, 2 },

  { 3, 1, 2, 3 },

  { 4, 3, 5, 4 } }

the amount of water can be trapped is 3, 

at position (1, 1) there is 2 units of water trapped,

at position (1, 2) there is 1 unit of water trapped.
"""
import heapq
class Solution(object):
    def max_water_trapped(self, matrix: list[list]) -> int:
        #high level idea: find the max water can be trapped on top of each bar. starting from edge lowest bar and traverse 4 directions

        if matrix == None or len(matrix) == 0:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False for j in range(n)] for i in range(m)]

        water_trapped= 0

        #define a priorityqueue for bfs algorithm
        minheap = []

        #initialize visited and queue by offer 4 edges elements to the queue       
        for y in range(n):
            heapq.heappush(minheap,(matrix[0][y], [0, y]))
            heapq.heappush(minheap,(matrix[m - 1][y], [m - 1, y]))
            visited[0][y] = True
            visited[m - 1][y] = True
        
        for x in range(1, m - 1):
            heapq.heappush(minheap, (matrix[x][0], [x, 0]))
            heapq.heappush(minheap, (matrix[x][n - 1], [x, n - 1]))
            visited[x][0] = True
            visited[x][n - 1] = True

        while minheap:
            curr = heapq.heappop(minheap)            
            curr_val = curr[0]
            curr_x = curr[1][0]
            curr_y = curr[1][1]

            #generate 4 neighbors and update matrix_path and water_trapped for each neighbor
            for x in [[0, 1],[0, -1],[1, 0],[-1, 0]]:
                next_x = curr_x + x[0]
                next_y = curr_y + x[1]
                if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n and (not visited[next_x][next_y]):
                    next_val = max(curr_val, matrix[next_x][next_y])
                    water_trapped += next_val - matrix[next_x][next_y]
                    heapq.heappush(minheap, (next_val, [next_x, next_y]))
                    visited[next_x][next_y] = True
                    
        return water_trapped