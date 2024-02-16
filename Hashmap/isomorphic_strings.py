"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
class Solution:
    def is_isomorphic(self, s: str, t: str) -> bool:
        map_s_to_t = {}
        map_t_to_s = {}
        

        for x in range(len(s)):
            c1 = s[x]
            c2 = t[x]
            if c1 not in map_s_to_t and c2 not in map_t_to_s:
                map_s_to_t.update({c1:c2})
                map_t_to_s.update({c2:c1})
            elif c1 not in map_s_to_t or c2 not in map_t_to_s:
                return False
            elif map_s_to_t.get(c1) != c2 or map_t_to_s.get(c2) != c1:
                return False
                
        return True
    
    """
        another solution:
        class Solution(object):
            def isIsomorphic(self, s, t):
                map1 = []
                map2 = []
                for idx in s:
                    map1.append(s.index(idx))
                for idx in t:
                    map2.append(t.index(idx))
                if map1 == map2:
                    return True
                return False
    """