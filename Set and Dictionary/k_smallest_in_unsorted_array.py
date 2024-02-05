"""
Find the K smallest numbers in an unsorted integer array A. The returned numbers should be in ascending order.

Assumptions

A is not null
K is >= 0 and smaller than or equal to size of A
Return

an array with size K containing the K smallest numbers in ascending order
Examples

A = {3, 4, 1, 2, 5}, K = 3, the 3 smallest numbers are {1, 2, 3}
"""
import heapq
class Solution(object):
    def k_smallest_in_unsorted_array(self, array: list, k: int) -> list:
        #use max heap to keep the current smallest element
        if not array or k == 0:
            return []

        heap = []
        for x in array:
            if len(heap) < k:
                heapq.heappush(heap, -x)
            elif x < -heap[0]:
                heapq.heapreplace(heap, -x)

        res = []
        while heap:
            res.append(-heapq.heappop(heap))

        res.reverse()
        return res
    

        


