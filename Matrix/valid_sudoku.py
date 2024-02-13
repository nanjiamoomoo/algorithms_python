"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

class Solution:
    def is_valid_sudoku(self, board: list[list[int]]) -> bool:
        #shortest solution:
        """
        
        1)It initializes an empty list called "res", which will be used to store all the valid elements in the board.

        2)It loops through each cell in the board using two nested "for" loops.
        For each cell, it retrieves the value of the element in that cell and stores it in a variable called "element".

        3)If the element is not a dot ('.'), which means it's a valid number, the method adds three tuples to the "res" list:

            The first tuple contains the row index (i) and the element itself.
            The second tuple contains the element itself and the column index (j).
            The third tuple contains the floor division of the row index by 3 (i // 3), the floor division of the column index by 3 (j // 3), and the element itself. 
                This tuple represents the 3x3 sub-grid that the current cell belongs to.
        4)After processing all the cells, the method checks if the length of "res" is equal to the length of the set of "res".
        """
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))
        """
        Standard Solution:
        #check each row
        for x in range(9):
            xset = set()
            for y in range(9):
                c = board[x][y]
                if c == ".":
                    continue
                if c in xset:
                    return False
                else:
                    xset.add(c)
                


        #check each column
        for y in range(9):
            yset = set()
            for x in range(9):
                c = board[x][y]
                if c == ".":
                    continue
                if c in yset:
                    return False
                else:
                    yset.add(c)


        #check each 3 x 3 grid
        for i in range(3):
            for j in range(3):
                gridset = set()
                for x in range(3):
                    for y in range(3):
                        c = board[x + 3 * i][y + 3 * j]
                        if c == '.':
                            continue
                        if c in gridset:
                            return False
                        else:
                            gridset.add(c)
        
        return True
        """
       