# Merge k Sorted Lists

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []

import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergek(serf, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        prev = dummy = ListNode(-1)       

        heap = []
        # we use i position just to make sure the heap item is completely comparable in case of equal values
        # heap compares the second element in case of the first element is equal
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            _, i, curr = heapq.heappop(heap)
            prev.next = curr
            prev = prev.next
            if prev.next:
                heapq.heappush(heap, (prev.next.val, i, prev.next))

        return dummy.next
