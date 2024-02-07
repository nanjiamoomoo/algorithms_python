"""
Given a singly-linked list, where each node contains an integer value, sort it in ascending order. 
The quick sort algorithm should be used to solve this problem.

Examples

null, is sorted to null
1 -> null, is sorted to 1 -> null
1 -> 2 -> 3 -> null, is sorted to 1 -> 2 -> 3 -> null
4 -> 2 -> 6 -> -3 -> 5 -> null, is sorted to -3 -> 2 -> 4 -> 5 -> 6
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solutoin(object):
    def quicksort_linkedlist(self, head) -> ListNode:
        """
            since this is linkedlist, we always pick the head position
            we split the list based on the head node

            Then we sort the left and sort the right
            then we comnnect them together and return
        """

        if head == None or head.next == None:
            return head
        
        # It is important to choose the head as pivot for faster process
        pivot = head
        head = head.next

        list1 = prev1 = ListNode(-1)
        list2 = prev2 = ListNode(-2)
        while head:
            if head.val <= pivot.val:
                prev1.next = head
                prev1 = prev1.next
            else:
                prev2.next = head
                prev2 = prev2.next
            head = head.next

        prev1.next = prev2.next = None #important to disconnect the two lists
        
        #sort left anr right
        first_half = self.quicksort_linkedlist(list1.next)
        second_half = self.quicksort_linkedlist(list2.next)

        pivot.next = second_half

        if first_half == None:
            return pivot
        
        curr = first_half
        while curr.next != None:
            curr = curr.next

        curr.next = pivot
        
        return first_half







