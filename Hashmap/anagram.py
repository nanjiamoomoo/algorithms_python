"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map1 = [0 for i in range(256)] #use ASCII code 
        map2 = [0 for i in range(256)]

        for idx in range(len(s)):
            map1[ord(s[idx])] += 1
            map2[ord(t[idx])] += 1

        return map1 == map2
    
    # if len(s) != len(t):
    #         return False
    # map1 = [0] * 26
    # map2 = [0] * 26

    # for idx in range(len(s)):
    #     map1[ord(s[idx]) - ord('a')] += 1
    #     map2[ord(t[idx]) - ord('a')] += 1

    # return map1 == map2

    """
    class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
            map1 = {}
            map2 = {}

            for idx in range(len(s)):
                map1.update({s[idx]: map1.get(s[idx], 0) + 1})
                map2.update({t[idx]: map2.get(t[idx], 0) + 1})
            
            return map1 == map2
    """