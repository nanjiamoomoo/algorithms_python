"""
Given a singly-linked list, where each node contains an integer value, sort it in ascending order. The selection sort algorithm should be used to solve this problem.

Examples

null, is sorted to null
1 -> null, is sorted to 1 -> null
1 -> 2 -> 3 -> null, is sorted to 1 -> 2 -> 3 -> null
4 -> 2 -> 6 -> 3 -> 5 -> null, is sorted to 2 -> 3 -> 4 -> 5 -> 6

"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    #do this inplace
    def selection_sort_linkedlist(self, head) -> ListNode:
        """
            key points:
            1. need to find out the max node for each cycle
            2. need to store the previous node of the max node, so we can connect the list. Just like to remove a node

            questions: do we need count the nodes that need to traverse? 
                we don't need to if we are not connecting the unsorted list to the sorted list
        """
        #corner case
        if head == None or head.next == None:
            return head
        # since there is a potential to change head
        prev = dummy = ListNode(-1)
        dummy.next = head

        newhead = None #this is the sorted list

        while prev.next != None:
            maxnodeprev = prev
            #step1: find max node on each cycle
            while prev.next != None:
                if prev.next.val > maxnodeprev.next.val:
                    maxnodeprev = prev
                prev = prev.next

            #we find out the previous node of maxnode, then we remove the maxnode from the orignal list and append it to the sorted list
            maxnode = maxnodeprev.next
            maxnodeprev.next = maxnode.next

            #append it to the sorted list
            maxnode.next = newhead
            newhead = maxnode

            prev = dummy

        return newhead
    

if __name__ == "__main__":
    node1 = ListNode(2)
    node2 = ListNode(1)
    node3 = ListNode(4)
    node4 = ListNode(-2)
    node5 = ListNode(-8)
    node6 = ListNode(10)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    head = node1

    sol = Solution()
    n = sol.selection_sort_linkedlist(head)
    while n != None:
        print(n.val)
        n = n.next

    
