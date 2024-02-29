"""
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

 

Example 1:


Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
0 <= Node.val <= 106
At most 105 calls will be made to hasNext, and next. 

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:
    """
        This is code for standard in order traversal
        res = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res
    """
    
    def __init__(self, root: TreeNode):
        self.stack = []
        self.curr = root

    def next(self) -> int:
        foundnext = False #identify if we have found the next element
        res = -1
        while self.stack or self.curr:
            if foundnext:
                break
            if self.curr:
                self.stack.append(self.curr)
                self.curr = self.curr.left
            else:
                self.curr = self.stack.pop()
                foundnext = True #if we already found the next element, we stop traversing
                res = self.curr.val
                self.curr = self.curr.right
        return res

    def hasNext(self) -> bool:
        return self.stack or self.curr
    

    """
    
    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
    
    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            current = node.right
            while current:
                self.stack.append(current)
                current = current.left
        return node.val
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0

    TC: next() has O(h) and hasNext() has O(1)
    SC: O(h)
    """

    # def __init__(self, root: TreeNode):
    #     self.inorder = []
    #     def dfs(root):
    #         if not root:
    #             return
    #         dfs(root.left)
    #         self.inorder.append(root.val)
    #         dfs(root.right)
    #     dfs(root)
    #     self.idx = 0

    # def next(self) -> int:
    #     if self.hasNext():
    #         self.idx += 1
    #         return self.inorder[self.idx - 1]
            

    # def hasNext(self) -> bool:
    #     return self.idx < len(self.inorder)
        
