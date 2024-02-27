"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

The number of nodes in the tree is in the range [1, 104].
-2^31 <= Node.val <= 2^31 - 1
"""
class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def is_valid_BST(self, root: TreeNode | None) ->  bool:
        min = float('-inf')
        max = float('inf')
        return self.dfs(root, min, max)
    

    #this dfs function returns if the tree with root node is BST or not
    def dfs(self, root, min, max) -> bool:
        if not root:
            return True
        
        if not (min < root.val < max):
            return False
        
        #if left Tree is not BST
        if not self.dfs(root.left, min, root.val):
            return False
        
        #if right Tree is not BST
        if not self.dfs(root.right, root.val, max):
            return False

        return True

