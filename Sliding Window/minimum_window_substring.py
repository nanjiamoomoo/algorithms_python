"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #we can use two pointers to similuate a sliding window
        char_dict = {}
        for x in t:
            if x in char_dict:
                char_dict[x] += 1
            else:
                char_dict[x] = 1

        left = 0
        match = 0# represents the count the matched characters in the sliding window
        res = ""
        """
            we need to keep moving the right boundary, until we find a a valid substring
            Then we move lef to make minimum the window
        """
        for right in range(len(s)):
            if s[right] in char_dict:
                count = char_dict[s[right]]
                count -= 1
                char_dict[s[right]] = count
                if count == 0: #remaining character in the window becomes zero means we found a match
                    match += 1
                while match == len(char_dict):# we can start moving left boundary                  
                    if s[left] in char_dict:
                        count = char_dict[s[left]]
                        count += 1
                        char_dict[s[left]] = count
                        if count == 1:
                            #we update here since this is the minimum window we can get with current right boundary
                            if res == "" or right - left + 1 < len(res): 
                                res = s[left:right + 1]
                            match -= 1       
                    left += 1        
        return res
