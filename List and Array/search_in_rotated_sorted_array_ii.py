"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
 
"""
class Solution:
    def search_in_rotated_sorted_array_ii(self, nums: list, target: int) -> bool:
        '''
            array is divided into two parts, the left ascending and the right ascending
            use binary search, left and right pointer
            if target == nums[left] then return True
            
            if target < nums[left] then it is in right ascenidng
                mid = target: return True
                mid < target: left = mid + 1
                mid > target: we have to check mid is in the left ascending or right ascending
                    here we have a problem, since the value could be the same
                    so in order to do binary search, we need to make sure the most left value != most right valve

                    once above step is done
                    it is the same problem as if there is no duplicate elemnets
                    if mid < mostLeft: right = mid - 1
                    if mid >= mostLeft: left = mid + 1
                
            if target > nums[left], it is in the left asxendint
                if mid = target: return true
                if mid > target: right = mid - 1
                if mid < target: 
                    if mid > rightMost: left = mid + 1
                    if mid <= rightMost: right = mid - 1

            else: it is in the left ascending

           
        '''
        left = 0
        right = len(nums) - 1
        if nums[left] == target:
            return True
    
        #jump through all the equal elements
        while left <= right and nums[left] == nums[right]:
            right -= 1
        
        if left >= right:
            return False
        
        leftMost = nums[left]
        rightMost = nums[right]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            
            if nums[mid] >= leftMost:
                if leftMost <= target < nums[mid]:                    
                    right = mid - 1
                else:
                    left = mid + 1
            else:               
                if nums[mid] < target <= rightMost:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
"""
Alternative question:
Find the index i such that A[i] == T or return -1 if there is no such index.

There could be duplicate elements in the array.
Return the smallest index if target has multiple occurrence. 
if len(nums) <= 0:
    return -1

left = 0
right = len(nums) - 1
if nums[left] == target:
    return left

#jump through all the equal elements
while left <= right and nums[left] == nums[right]:
    right -= 1

if left >= right:
    return -1

leftMost = nums[left]
rightMost = nums[right]

while left < right:
    mid = (left + right) // 2        
    
    if nums[mid] >= leftMost:
        if leftMost <= target <= nums[mid]:                    
            right = mid
        else:
            left = mid + 1
    else:               
        if nums[mid] < target <= rightMost:
            left = mid + 1
        else:
            right = mid

if nums[left] == target:
    return left

return -1
"""
    
    