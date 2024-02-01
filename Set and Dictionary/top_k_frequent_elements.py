"""
iven an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # thisdict = {}
        # for x in nums:
        #     count = thisdict.get(x)
        #     thisdict.update({x : count + 1 if count != None else 1})

        # heap = []
        # for key, value in thisdict.items():
        #     if len(heap) < k:
        #         heapq.heappush(heap, (value, key))
        #     elif value > heap[0][0]:
        #         heapq.heapreplace(heap, (value, key))
        
        # res = []
        # while heap:
        #     res.append(heapq.heappop(heap)[1])

        # res.reverse
        # return res

        orb = {}

        for i in nums:
            if i in orb:
                orb[i] += 1
            else: orb[i] = 1
        
        sorted_orb = sorted(orb, key=orb.get, reverse=True)
        return sorted_orb[:k]