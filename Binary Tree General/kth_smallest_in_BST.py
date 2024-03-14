"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(root) -> bool:
            nonlocal ans, k
            if not k:
                return True
            if not root:
                return False           
            if inorder(root.left): #early terminiation
                return True
            ans = root.val
            k -= 1
            if inorder(root.right):
                return True
        ans = None
        inorder(root)
        return ans
