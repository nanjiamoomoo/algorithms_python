"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: list) -> int:
        #we can use sliding window to solve the problem
        #two pointesr, [left, right) represents the left and right boundary of the sliding window
        #condition to move right: when the sum in the window is less than 7
        #condition to move left： whent the sum int he window is not less than 7

        left = right = 0
        n = len(nums) 
        min_len = n + 1
        window_sum = 0 
        while left < n and right <= n:
            if window_sum < target: 
                if right == n: #if the right already reaches to the end, and sum < target, we can break
                    break         
                window_sum += nums[right]      
                right += 1            
            else:
                min_len = min(right - left, min_len)
                window_sum -= nums[left]
                left += 1
            
        min_len = min_len if min_len <= n else 0
        return min_len
    
    def minSubArrayLenII(self, target: int, nums: list) -> int:
        #we can use sliding window to solve the problem
        #two pointesr, [left, right] represents the left and right boundary of the sliding window, inclusive on both ends
        #condition to move right: when the sum in the window is less than 7
        #condition to move left： whent the sum int he window is not less than 7

        """
        class Solution:
            def minSubArrayLen(self, target: int, nums: List[int]) -> int:
                l=0
                total=0
                ans=float("inf")
                n=len(nums)
                for r in range(n):
                    total+=nums[r]
                    while total>=target:
                        ans=min(r-l+1,ans)
                        total-=nums[l]
                        l+=1

                return 0 if ans==float("inf") else ans       
        """

        left = right = 0
        n = len(nums) 
        min_len = n + 1
        window_sum = nums[0]
        while left < n and right < n:
            if window_sum < target:                         
                right += 1
                if right == n: #if the right already reaches to the end, and sum < target, we can break
                    break     
                window_sum += nums[right]               
            else:
                min_len = min(right - left + 1, min_len)
                window_sum -= nums[left]
                left += 1
            
        min_len = min_len if min_len <= n else 0
        return min_len
    
    