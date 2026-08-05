class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #this is a topological sort problem/cycle detection
        #given: an array preqreusities and the number of courses to take
        #return: whether it is possible to finish all courses
        #solution: use kahn's algorithm
        
        graph = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites: 
            graph[pre].append(course)
            indegree[course] += 1
        
        #now we have an adjacency list with the dependencies 

        q = [c for c in range(numCourses) if indegree[c] == 0]
            
        #now we have all the nodes that start with zero dependencies

        finished = 0 
        while q: 
            curr = q.pop()
            finished += 1
            for nxt in graph[curr]: 
                indegree[nxt] -= 1
                if indegree[nxt] == 0: 
                    q.append(nxt)

        return bool(finished == numCourses)

