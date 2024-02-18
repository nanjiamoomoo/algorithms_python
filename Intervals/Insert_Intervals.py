"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        #we need to find the two intervals in the list
        #1. the first interval (i) that interval[1] >= newInterval[0]
        #2. the last interval (j) that interval[0] <= newInteveral[1]
        # all the interval between [i, j] needs to merge with the new interval
        # i is the position where we should insert the new merged interval

        i = len(intervals)
        j = -1
        foundi = False
        for idx in range(len(intervals)):
            curr_interval = intervals[idx]
            if curr_interval[1] >= newInterval[0] and not foundi:
                i = idx
                foundi = True
            if curr_interval[0] <= newInterval[1]:
                j = idx
        
        if (j >= i):
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[j][1])
            for _ in range(j - i + 1):
                intervals.pop(i)
        
        intervals.insert(i, newInterval)
        return intervals
    
    """
    Deep copy solution:
        # Initialize an output container
        output = []

        # Iterate through all intervals
        for i in range(len(intervals)):
            # If the new interval ends before the current interval
            # - Append the new interval to the output
            # - Append the rest of the remaining intervals to the output
            # - Return the output
            if newInterval[1] < intervals[i][0]:
                output.append(newInterval)
                return output + intervals[i:]
            
            # If the new interval begins after the current interval
            # - Append the current interval to the output
            elif newInterval[0] > intervals[i][1]:
                output.append(intervals[i])

            # If the new interval overlaps with the current interval
            # merge intervals to create a new interval where
            # - Interval begins at the earliest of beginnings
            # - Interval ends at the latest of ends
            #
            # ! Do not add the new interval to the output just yet!
            # ! Further merging may be required
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        # Add the new interval to the output if not added already
        # ! No need for conditions as we would not reach this point otherwise
        output.append(newInterval)

        # Return the final output
        return output
    
    """


