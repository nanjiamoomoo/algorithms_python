"""

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        #this function returns the max path from any node to the current root
        def maxPath(root, res) -> int:
            #base case
            if not root:
                return 0

            left = maxPath(root.left, res)
            right = maxPath(root.right, res)

            #if left is < 0, we ignore
            left = max(left, 0)
            right = max(right, 0)

            #need to update max that passes current root
            res[0] = max(res[0], left + right + root.val)

            return root.val + max(left, right)

        res = [float('-inf')]
        maxPath(root, res)
        return res[0]
