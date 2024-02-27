"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        #prev represents the previous node that we kept (no duplicates)
        prev = dummy = ListNode(-1)
        curr = dummy.next = head #curr is the node we are checking
        while prev.next:
            first = curr #first is the first node with the same value
            count = 0
            while curr and curr.val == first.val:
                curr = curr.next
                count += 1
            if count == 1:
                prev.next = first
                prev = prev.next
            else:
                prev.next = curr
        return dummy.next