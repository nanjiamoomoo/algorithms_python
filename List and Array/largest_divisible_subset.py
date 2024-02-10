"""
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.
"""

class Solution:
    def largestDivisibleSubset(self, nums: list) -> list:
      #use dp to solve the problem
        #dp[i] represents the largest thisdict subset ending at index i
        # for each index j between [0, i) we need to check if we can inherit the previous subset at index j

        #sort first
        nums.sort()
        lds = [[x] for x in nums] #list comprehension
        max = 0 #the global max index position
        for i in range(1, len(nums)):
            curr = -1 # default value
            for j in range(i):
                if nums[i] % nums[j] == 0 and (curr == -1 or len(lds[j]) > len(lds[curr])):
                    curr = j
            if curr != -1:
                lds[i].extend(lds[curr])
            if len(lds[i]) > len(lds[max]):
                max = i
        
        return lds[max]
        
        

if __name__=="__main__":
    sol = Solution()
    nums = [1,2,3]
    print(sol.largestDivisibleSubset(nums))
