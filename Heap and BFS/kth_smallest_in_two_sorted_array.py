"""
Given two sorted arrays A and B, of sizes m and n respectively. 
Define s = a + b, where a is one element from A and b is one element from B. Find the Kth smallest s out of all possible s'.

Assumptions

A is not null and A is not of zero length, so as B
K > 0 and K <= m * n
Examples

A = {1, 3, 5}, B = {4, 8}

1st smallest s is 1 + 4 = 5
2nd smallest s is 3 + 4 = 7
3rd, 4th smallest s are 9 (1 + 8, 4 + 5) 
5th smallest s is 3 + 8 = 11
"""
import heapq
class Solution:
    def kth_smallest_in_two_sorted_array(self, a: list, b: list, k: int) -> int:
        visited = []
        for x in a:
            for y in b:
                visited.append(False)
        
        heap = []
        heapq.heappush(heap, (a[0] + b[0], 0, 0))
        visited[0] = True

        while k > 1:
            curr = heapq.heappop(heap)
            for x, y in ([curr[1] + 1, curr[2]],[curr[1], curr[2] + 1]):
                if 0 <= x < len(a) and 0 <= y < len(b) and not visited[len(b) * x + y]:
                    heapq.heappush(heap, (a[x] + b[y], x, y))
                    visited[len(b) * x + y] = True
            k -= 1

        return heapq.heappop(heap)[0]

if __name__ == "__main__":
    a = [1,1,1,1,1,1,1,1,1,1,11,12]
    b = [1,12,200]
    k = 22

    sol = Solution()
    res = sol.kth_smallest_in_two_sorted_array(a, b, k)
    print(res)