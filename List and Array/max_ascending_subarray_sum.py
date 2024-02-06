"""
Given an array of integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. 
Note that a subarray of size 1 is ascending.

 

Example 1:

Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
Example 2:

Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
Example 3:

Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.

"""

class Solution:
    def max_ascending_subarray_sum(self, nums: list) -> int:

        #question: when shall we inherit the previous subarray sum?
        #  when it is ascending and also the previous subarray sum is non-negative  


        curr = 0 # represents the max ascending subarray sum at current index(inclusive)
        global_max = int('-inf')

        for i in range(len(nums)):
            if curr >= 0 and i > 0 and nums[i] > nums[i - 1]:
                curr += nums[i]
            else:
                curr = nums[i]
            global_max = max(global_max, curr)
        
        return global_max
      