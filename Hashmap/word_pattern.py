"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""
class Solution:
    def word_pattern(self, pattern:str, s:str) -> bool:
        #this is similar to the isomorphic question
        list1 = list(pattern)
        list2 = s.split(' ')

        map1 = []
        map2 = []
        if len(list1) != len(list2):
            return False

        for idx in range(len(list1)):
            map1.append(list1.index(list1[idx]))
            map2.append(list2.index(list2[idx]))

        return map1 == map2
    
    """
        Nother solution:
        map1 = {}
        l = s.split(" ")
        if len(pattern) != len(l):
            return False
        map2 = {}

        for idx in range(len(l)):
            c = pattern[idx]
            word = l[idx]
            if c not in map1 and word not in map2:
                map1.update({c:word})
                map2.update({word:c})
            elif c not in map1 or word not in map2:
                return False
            elif map1.get(c) != word or map2.get(word) != c:
                return False

        return True
    """