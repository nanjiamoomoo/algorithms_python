"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
from collections import deque
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        #BFS solution
        #we can change direclty on the original grid matrix, but it needs to be clarified. 
        visited = []
        for x in range(len(grid)):
            visited.append([])
            for y in range(len(grid[0])):
                visited[x].append(int(grid[x][y]))
        
        islands_num = 0
       

        def bfs(visited : list[list[int]], x: int, y:int):
            queue = deque()
            queue.append([x, y])
            while queue:
                curr = queue.popleft()
                for i, j in ([curr[0], curr[1] + 1], [curr[0] + 1, curr[1]], [curr[0] - 1, curr[1]], [curr[0], curr[1] - 1]):
                    if 0 <= i < len(visited) and 0 <= j < len(visited[0]) and visited[i][j]:
                        visited[i][j] = 0
                        queue.append([i, j])
                        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if visited[x][y]:
                    visited[x][y] = 0
                    bfs(visited, x, y)
                    islands_num += 1

        return islands_num
    
    """
    #DFS solution. 
        visited = []
        for x in range(len(grid)):
            visited.append([])
            for y in range(len(grid[0])):
                visited[x].append(int(grid[x][y]))
        
        islands_num = 0
       

        def dfs(visited : list[list[int]], x: int, y:int):
            if not 0 <= x < len(visited):
                return
            if not 0 <= y < len(visited[0]):
                return
            if not visited[x][y]:
                return            
            visited[x][y] = 0
            for i, j in ([x + 1, y], [x, y + 1], [x, y - 1], [x - 1, y]):
                dfs(visited, i, j)
           
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if visited[x][y]:
                    dfs(visited, x, y)
                    islands_num += 1

    
    """