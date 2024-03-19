"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = [None]
        def dfs(root, prev):
            if not root:
                return            
            left = root.left
            right = root.right
            if prev[0]:
                prev[0].right = root            
            prev[0] = root
            root.left = None
            
            dfs(left, prev)
            dfs(right, prev)
        
        dfs(root, prev)
        return root
        """
        Iteratively Method:

        if not root:
             return root
        stack = [root]
        prev = None
        while stack:
            curr = stack.pop()  
            if prev:
                prev.right = curr
            #stack is last in first out       
            if curr.right: #if it has right subtree, we put it in first
                stack.append(curr.right)
            if curr.left: #if it has left, we put it in after right
                stack.append(curr.left)    
            #after curr.left and curr.right are in stack, we can change curr 
            curr.left = None               
            prev = curr         
        return root
        
        """
      