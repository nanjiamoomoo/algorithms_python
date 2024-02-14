"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
"""
class Solution:
    def game_of_life(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board:
            return
        
        #check each cell's next state and stores them in a separate array
        m = len(board)
        n = len(board[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        for x in range(m):
            for y in range(n):
                livecells = 0
                for i, j in directions:
                    if 0 <= x + i < m and 0 <= y + j < n and abs(board[x + i][y + j]) == 1:
                        livecells += 1
                if board[x][y] == 0 and livecells == 3:
                    #we use 2 to represents original cell was 0, but now is live
                    board[x][y] = 2                    
                elif board[x][y] == 1 and (livecells < 2 or livecells > 3):
                    #we use -1 to represents orignal cell was 1, but now is dead
                    board[x][y] = -1
              

        for x in range(m):
            for y in range(n):
                if board[x][y] == -1:
                    board[x][y] = 0
                elif board[x][y] == 2:
                    board[x][y] = 1

        #TC: O(m*n)
        #SC: O(1)