"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #here is algorithm
        #step1: we sorted the intervals based on the start time from early to late
        #step2: we traverse through intervals and compare the start time with previous interval end time
        #step3: if they overlap, mwe update current interval end time and keep going to the next interval
        #step4: if they don't overlap, means we find a interval, we update resulat and start over step2 and 3
        res = []
        list.sort(intervals, key= lambda x : x[0])

        j = 0        
        while j < len(intervals):
            i = j   
            end = intervals[j][1]         
            while j < len(intervals) and intervals[j][0] <= end:
                end = max(end, intervals[j][1])
                j += 1
            res.append([intervals[i][0], end])
        return res