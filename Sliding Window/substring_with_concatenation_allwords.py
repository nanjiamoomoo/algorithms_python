"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
The output order does not matter. Returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: Since words.length == 4 and words[i].length == 4, the concatenated substring has to be of length 16.
There is no substring of length 16 in s that is equal to the concatenation of any permutation of words.
We return an empty array.
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.
 

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""

class Solution:
    def findSubstring(self, s: str, words: list) -> list:
        #we can a sliding window of fixed lenth to solve the problem
        #the fixed length equals to the total length of words in the words list

        nums = len(words)
        word_len = len(words[0])
        total_len = nums * word_len
        #the potential substring starting indices are in the range of [0, len(s) - total_len]
        
        res = []
        if (len(s) < total_len):
            return res

        #we can use dictionaly to check match
        thisdict = {}
        for word in words:
            if word in thisdict:
                thisdict[word] += 1
            else:
                thisdict[word] = 1

        #i is the displacement in the word. This makes the travesal a lot faster, since we can move with step of "word_len"
        for i in range(word_len):
            left = i #represents the left boundary of the sliding window
            count = 0 # this represents the count of the words in the sliding window
            curr_dict = {} #this acts as the sliding window for match check
            #j is the stargin indices of each word we are checking
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word in thisdict:
                    curr_dict[word] = curr_dict.get(word, 0) + 1
                    count += 1

                    while curr_dict[word] > thisdict[word]:
                        left_word = s[left:left + word_len]
                        curr_dict[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == len(words):
                        res.append(left)
                else:
                    curr_dict.clear()
                    count = 0
                    left = j + word_len #sliding window length became zero

        return res
            
if __name__ == "__main__":
    s = "barfoofoobarthefoobarman"
    words =["foo","bar", "the"]
    sol = Solution()
    res = sol.findSubstring(s, words)
    print(res)

                       
        # for i in range(0, len(s) - total_len + 1):
        #     curr_dict = {}
        #     for j in range(i, i + total_len - word_len + 1, word_len):
        #         curr_word = s[j:j+word_len]
        #         if curr_word in curr_dict:
        #             curr_dict[curr_word] += 1
        #         else:
        #             curr_dict[curr_word] = 1
        #         # count = curr_dict.get(curr_word)
        #         # curr_dict.update({curr_word: count + 1 if count is not None else 1})
        #     #check if curr_dict matches the thisdict
        #     match = True
        #     for x in thisdict:
        #         if thisdict.get(x) != curr_dict.get(x):
        #             match = False
        #             break
                
        #     if match:
        #         res.append(i)
        
        # return res
