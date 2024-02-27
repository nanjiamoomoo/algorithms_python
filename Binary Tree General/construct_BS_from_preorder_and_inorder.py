"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        mp = {}
        for idx in range(len(inorder)):
            mp.update({inorder[idx] : idx})
        
        def constructor(preorder: list, preleft: int, preright:int, inorder: list, inleft:int, inright: int, mp: dict) -> TreeNode:
            if preleft > preright:
                return None            
            val = preorder[preleft]
            root = TreeNode(preorder[preleft])

            idx = mp[val]
            # leftnodecount = idx - inleft
            # rightnodecount = inright - idx
            left = constructor(preorder, preleft + 1, preleft + idx - inleft, inorder, inleft, idx - 1, mp)
            right = constructor(preorder, preleft + idx - inleft + 1, preright, inorder, idx + 1, inright, mp)

            root.left = left
            root.right = right
            return root

        return constructor(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, mp)
