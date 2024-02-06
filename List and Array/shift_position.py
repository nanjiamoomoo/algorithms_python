"""
Given an integer array A, A is sorted in ascending order first then shifted by an arbitrary number of positions, 
For Example, A = {3, 4, 5, 1, 2} (shifted left by 2 positions). Find the index of the smallest number.

Assumptions

There are no duplicate elements in the array
Examples

A = {3, 4, 5, 1, 2}, return 3
A = {1, 2, 3, 4, 5}, return 0
Corner Cases

What if A is null or A is of zero length? We should return -1 in this case.
"""

class Solution:
    def shift_position(self, array: list) -> int:

        """
            the smallest index must satisfy the following
            it's left element is bigger than it self

            corner case:
            array == None or len(array) == 0

            shift = 0: 

            binary search
            left, right

            mid < mid - 1: return mid
            mid > mid - 1:
                if mid <= mostRight: right = mid - 1
                if mid > mostRight: left = mid + 1 
        """

        if not array:
            return -1

        left = 0
        right = len(array) - 1
        left_most = array[left]
        right_most = array[right]
        if left_most < right_most:
            return 0
        
        while left < right - 1:
            mid = (left + right + 1) // 2 # we use right mid since we need to use mid - 1 index, so that we don't need to stop the cycle when there are only 2 elements
            if array[mid] < array[mid - 1]: 
                return mid
            else:
                if array[mid] <= right_most:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return left if array[left] < array[right] else right
    
    """
        Another solution:
        Binary Search:
        left right

        while left < right
            if array[left] < array[right] return left: since the searching space is sorted

            if mid >= leftMost: left = mid + 1
            else: right = mid # the smallest index on the right ascending sequence

        return left

    """
                
