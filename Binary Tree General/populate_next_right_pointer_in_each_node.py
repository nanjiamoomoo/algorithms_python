"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Constraints:

The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100
 
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
import collections
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        #we can us BFS algorithm
        if not root:
            return root
        
        #we use collections.deque() since it has O(1) in the popleft() operation versus list O(n) in pop(0)
        #however in real run time testing, list() maybe faster since there is no library import needed and the tree is not too wide. 
        queue = collections.deque()
        queue.append(root)
        while queue:
            size = len(queue)            
            prev = None
            for _ in range(size):
                curr = queue.popleft()
                if prev:
                    prev.next = curr
                prev = curr
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return root