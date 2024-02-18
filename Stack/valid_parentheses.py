"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
class Solution:
    def valid_parentheses(self, s:str) -> bool:
        #we can use stack to solve the problem
        stack = []
        mp = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for c in s:
            #when to return false
            if c in mp and (not stack or mp.get(c) != stack[-1]):
                return False
            #when to add
            elif c not in mp:
                stack.append(c)
            #when to pop
            else:
                stack.pop()
    
        return not stack
