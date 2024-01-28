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

class Solution:
    def course_schedule(self, course_number : int, prerequisites: list[list[int]]) -> list[int]:
        #define return list
        res = [] 
        #corner case
        if course_number == 0:
            return res
        
        #visited list
        visited = [0] * course_number    

        #define adjacency list for neighbor iteration
        adj_list = []
        for x in range(course_number):
            adj_list.append([])

        #add values to adjancey list
        for x in prerequisites:
            adj_list[x[1]].append(x[0])

    
        for x in range(course_number):
            if self.has_cycle(adj_list, res, visited, x):
                return []

        res.reverse()
        return res



    def has_cycle(self, adj_list: list[list[int]], res: list[int], visited: list[int], course: int) -> bool:
    
        """
            visited[x] == 2: loop completed
            visited[x] == 1: currently traversing
            vistied[x] == 0: has not been visited
        """
        if (visited[course] == 2):
            return False
    
        #find a cycle
        if (visited[course] == 1):
            return True
            
        visited[course] = 1
        for x in adj_list[course]:
            if self.has_cycle(adj_list, res, visited, x):
                return True
            
        visited[course] = 2
        res.append(course)
        return False
        


class Test(object):
    sol = Solution()
    course_number = 4
    prerequisites = [[1,0], [2, 0], [3, 1], [3, 2]]
    print(sol.course_schedule(course_number, prerequisites))