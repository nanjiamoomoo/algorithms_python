
#Course Schedule

"""
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""

import collections
class Solution:
    def course_schedule(self, course_number : int, prerequisites: list[list[int]]) -> list[int]:
        #define return list
        res = [] 
        #corner case
        if course_number == 0:
            return res
        
        #defind indegree map/list, each index represents a course
        ind_map = []
        #define adjacency list for neighbor iteration
        adj_list = []

        #initialize indegree map and adjacency list
        for x in range(course_number):
            ind_map.append(0)
            adj_list.append([])

        #add values to the indegree map and adjancey list
        for x in prerequisites:
            ind_map[x[0]] += 1
            adj_list[x[1]].append(x[0])

        #define queue
        queue = collections.deque()
        #initialize queue
        for x in range(course_number):
            if ind_map[x] == 0:
                queue.append(x)

        #use bfs algorithms to do topological sorting
        while len(queue) != 0:
            curr = queue.popleft()
            res.append(curr)
            #generate it's neighbors
            for x in adj_list[curr]:
                # reduce it's neibor indegree by 1 and update queeu 
                ind = ind_map[x]
                ind -= 1
                ind_map[x] = ind
                if ind == 0:
                    queue.append(x)

        return res if len(res) == course_number else []

class Test(object):
    sol = Solution()
    course_number = 4
    prerequisites = [[1,0], [2, 0], [3, 1], [3, 2]]
    print(sol.course_schedule(course_number, prerequisites))