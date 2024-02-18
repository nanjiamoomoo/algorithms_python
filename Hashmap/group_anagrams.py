"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
class Solution:
    def group_anagrams(self, strs: list) -> list[list]:
        #this solution is crazy
        mp = {}
        res = []

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in mp:
                res[mp[sorted_s]].append(s)
            else:
                mp[sorted_s] = len(res)
                res.append([s])
        return res
    
    """
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
    """

        # res = []
        # if len(strs) == 1:
        #     res.append(strs)
        #     return res
        # res = []
        # if len(strs) == 1:
        #     res.append(strs)
        #     return res
            

        # def anagrams(s, t) -> bool:
        #     if len(s) != len(t):
        #             return False
        #     list1 = [0 for i in range(26)]
        #     list2 = [0 for i in range(26)]

        #     for idx in range(len(s)):
        #         list1[ord(s[idx]) - ord('a')] += 1
        #         list2[ord(t[idx]) - ord('a')] += 1
        #     return list1 == list2
        
        # arr = [i for i in range(len(strs))]

        # def union(i:int, j:int):
        #     rooti = find(i)
        #     rootj = find(j)
        #     if rooti <= rootj:
        #         arr[rootj] = rooti
        #     else:
        #         arr[rooti] = rootj
        
        # def find(x:int) -> int:            
        #     if x == arr[x]:
        #         return x
        #     arr[x] = find(arr[x])
        #     return arr[x]
        
        # for i in range(len(strs)):
        #     for j in range(i + 1, len(strs)):
        #         if anagrams(strs[i], strs[j]):
        #             union(i, j)
        
        # map = {}
        # for idx in range(len(strs)):
        #     if arr[idx] in map:
        #         map.get(arr[idx]).append(strs[idx])
        #     else:
        #         currlist = list()
        #         currlist.append(strs[idx])
        #         map.update({arr[idx]: currlist})
        # return list(map.values())
    
if __name__ == "__main__":
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    res = sol.group_anagrams(strs)
    print(res)
                          
                
                          
                
                     
                

                    
                        
                  


