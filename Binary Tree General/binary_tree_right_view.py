"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.


Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        res = []
        if not root:
            return res
        queue = deque()        
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if i == size - 1:
                    res.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return res
    #Nother Solution dfs
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     res = []
    #     def dfs(root, depth):
    #         if not root:
    #             return
            
    #         if depth == len(res):
    #             res.append(root.val)
    #         dfs(root.right, depth + 1)
    #         dfs(root.left, depth + 1)

    #     dfs(root, 0)
    #     return res