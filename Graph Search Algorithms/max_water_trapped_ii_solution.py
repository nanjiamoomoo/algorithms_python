"""
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

 

Example 1:


Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
Example 2:


Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
 

Constraints:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 104
"""
import heapq
class Solution(object):
    def max_water_trapped(self, heightMap: list[list]) -> int:
        #from the lowest edge bar and update water trapped on top of it and traverse 4 directions
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])

        # if one edge length smaller than 3, there is no water can be trapped
        if m < 3 or n < 3:
            return 0
        #use heap to find the lowest board, heap keeps all the boarder elements positions with the lowest path height
        heap = []

        #initialize heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1 # represents the bar has been visited

       
        res = 0

        while heap:
            height, i, j = heapq.heappop()
            
            for x, y in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and heightMap[x][y] != -1:
                    #update lowest height edge at x, y position
                    level = max(height, heightMap[x][y])

                    #update water trapped on top of x, y position
                    res += level - heightMap[x][y]

                    #update heap
                    heapq.heappush(heap, (level, x, y))

                    #update x, y as visited
                    heightMap[x][y] = -1


        return res