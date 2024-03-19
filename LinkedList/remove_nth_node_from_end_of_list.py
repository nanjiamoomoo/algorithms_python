"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def remove_nth_node_from_end(self, head: ListNode, n: int) -> ListNode:
        #method 1: find the node first and remove. This method passes the list twice
        # count = 0
        # prev = dummy = ListNode(-1)
        # dummy.next = head
        # while prev.next:
        #     count += 1
        #     prev = prev.next        
        # count -= n
        # prev = dummy
        # while count:
        #     prev = prev.next
        #     count -= 1
        # prev.next = prev.next.next
        
        # return dummy.next

        #method2: pass the list once with SC O(1)
        #sliding window idea, we can find the node to be removed as long as we keep the distance of (n - 1) with the current node

        #prev represents the node before the node to be deleted
        prev = dummy = ListNode(-1)
        curr = dummy.next = head
        count = 0 #represents how many nodes passed

        while curr:
            #the distance between curr and head should be n
            if count >= n:
                prev = prev.next
            curr = curr.next
            count += 1

        prev.next = prev.next.next
        return dummy.next
            



        
        
        










