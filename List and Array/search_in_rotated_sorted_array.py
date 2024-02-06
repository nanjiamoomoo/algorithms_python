"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
 
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

"""
class Solution:
    def search_in_rotated_sorted_array(self, nums: list, target:int) -> int:
        
        #use binary search, the array can be divided into left ascending and right ascending
        """            
            1. mid == target return
            2. mid >= left: mid falls under the left ascending sequence
                2.1 mid < target: left = mid + 1
                2.2 mid > target: 
                    2.2.1： if target >= left: right = mid - 1
                    2.2.2: if target < left: left = mid + 1
            3. mid < left: mid falls under the right ascending sequence
                3.1 mid < target:
                    3.1.1: target <= right: left = mid + 1
                    3.1.2: target > right: right = mid - 1
                3.2 mid > target: right = mid - 1
        """
        if len(nums) <= 0:
            return -1
        i = 0
        j = len(nums) - 1
        left = nums[i]
        right = nums[j]

        while i <= j:
            mid = i + int((j - i) / 2)
            if nums[mid] == target:
                return mid
            curr = nums[mid]
            if curr >= left:
                if curr < target or target < left:
                    i = mid + 1
                else:
                    j = mid - 1            
            else:
                if curr > target or right < target:
                    j = mid - 1
                else: 
                    i = mid + 1
        return -1
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.search_in_rotated_sorted_array([20,30,2,12,13,14,15],30))

    

