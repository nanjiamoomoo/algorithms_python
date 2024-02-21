"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
"""
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #high level idea:
        """
            1. break the list into 3 parts
                list before left
                list between left and right
                list after right
            2. reverse the list between left and right`
            3. connect them together

        """
        headone = tailone = headtwo = tailtwo = headthree = None

        curr = head
        count = 1
        if left > 1:
            headone = head
        while curr:
            if count == left - 1:
                tailone = curr
            if count == left:
                headtwo = curr
            if count == right:
                tailtwo = curr
            if count == right + 1:
                headthree = curr
            count += 1
            curr = curr.next
        
        #now reverse the list between left and right
        tailtwo.next = None
        prev = None
        curr = headtwo
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode

        #now reverse tailtwo and headtwo:
        [headtwo, tailtwo] = [tailtwo, headtwo]
        #now connects them together
        tailtwo.next = headthree

        if headone is None:
            return headtwo
        
        tailone.next = headtwo
        return headone
    
    """
        Another way to use one loop:
        since there is a chance to change head, so we use a dummy node to help

        prev = dummy = ListNode(-1)
        prev.next = head

        count = 1
        while prev.next:
            #this is where we do reverse operation
            if count == left:
                tail = prev
                curr = prev.next
                prev = None
                #reverse logic
                while count <= right:
                    nextnode = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nextnode
                    count += 1
                tail.next.next = curr #connect the tail.next to the remaining list after "right" position
                tail.next = prev #connect the tail node to the new head after reverse
                break
            prev = prev.next
            count += 1
        return dummy.next
    
    """

