"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
 

Constraints:

1 <= words.length <= 500
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]
 

Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
"""

import heapq

class StringObject(object):
    def __init__(self, key):
        self.key = key
    def __lt__(self, other):
        return self.key > other.key
    def __eq__(self, other):
        return self.key == other.key
    
class Solution(object):
    def top_k_frequent_words(self, words: list, k: int) -> list:
        #step1: convert the words list to dictionary with {name, count} as the value pair
        #step2: define min heap to compare based on 1. count 2. name-> lexicographical order
        #step3: maintain the heap with size k to keep the current top k frequent words
        #step4: pop elements from one by one to make the final return list

        words_dict = {}
        for x in words:
            count = words_dict.get(x)
            words_dict.update({x : count + 1 if count != None else 1})
            # if count:
            #     dict.update({x: count + 1})
            # else:
            #     dict.update({x: 1})

        heap = []
        count = 0
        for key, value in words_dict.items():
            if count < k:
                heapq.heappush(heap, (value, StringObject(key)))
                count += 1
            
            else:
                pair = heap[0]
                if value > pair[0] or (value == pair[0] and key < pair[1].key):
                    heapq.heapreplace(heap, (value, StringObject(key)))
                    
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1].key)

        res.reverse()

        return res
        