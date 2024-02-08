"""
Word “book” can be abbreviated to 4, b3, b2k, etc. Given a string and an abbreviation, return if the string matches the abbreviation.

Assumptions:

The original string only contains alphabetic characters.
Both input and pattern are not null.
Pattern would not contain invalid information like "a0a","0".
Examples:

pattern “s11d” matches input “sophisticated” since “11” matches eleven chars “ophisticate”.
"""
class Solution(object):
  def match(self, input, pattern):
    """
    input: string input, string pattern
    return: boolean
    """
    # write your solution here
    one = two = 0

    while one < len(input) and two < len(pattern):
      is_digit = pattern[two].isnumeric()
      #scenario one: pattern[two] is digit
      if is_digit:
        begin = two
        while two < len(pattern) and pattern[two].isnumeric():
          two += 1
        s = pattern[begin:two]
        num = int(s)
        one += num
      #scenario two: pattern[two] is not digit
      else:
        if input[one] != pattern[two]:
          return False
        else:
          one += 1
          two += 1
    
    return True if one == len(input) and two == len(pattern) else False

#test
if __name__ == "__main__":
  input = "sophisticated"
  pattern = "s11d"
  sol = Solution()
  print(sol.match(input, pattern))
