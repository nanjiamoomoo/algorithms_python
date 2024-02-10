
"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
class Solution:
    def longest_substring(self, s: str) -> int:
        #sliding window [l, r]
        #if s[r] is unique, added to the current set
        #if it is not unit, move left until it is unique      
        l = 0
        charset = set()
        max_len = 0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            max_len = max(max_len, len(charset))
        return max_len
    
if __name__ == "__main__":
    str = "abcabcbb"
    sol = Solution()
    res = sol.longest_substring(str)
    print(res)
