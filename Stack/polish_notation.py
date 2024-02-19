"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""

class Solution:
    def eval_reverse_polish_notation(self, tokens: lsit[str]) -> int:
        #we can use a stack to help
        """
        Operation rules:
        1. for new element if it a number, we push it in the stack
        2. if it is an operator, we take the top 2 elements out and calculate with the operator and put it back in stack
        3. the last element remaining in the stack is the result
        """
        stack = []
        operators = {"+", "-", "*", "/"}
        def calulator(a:str, b:str, operator:str) -> int:
            if operator == '+':
                return int(a) + int(b)
            elif operator == '-':
                return int(a) - int(b)
            elif operator == '*':
                return int(a) * int(b)
            else:
                return int(int(a) / int(b))
        
        for x in tokens:
            if x not in operators:
                stack.append(x)
            else:
                b = stack.pop()
                a = stack.pop()
                result = calulator(a, b, x)
                stack.append(str(result))
        return int(stack.pop())
