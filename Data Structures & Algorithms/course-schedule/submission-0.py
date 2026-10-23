class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #  look for cycles in the graph and if there is a cycle hen false otherwise it is true
        seen = set()
        seeing = set()
        graph = {}

        for i in range(numCourses):
            graph[i] = []

        for course, pre in prerequisites:
            graph[course].append(pre)
        print(graph)

        def dfs(course):
            if course in seeing:
                return False
            if course in seen:
                return True
            seeing.add(course)
            for pre in graph[course]:
                resultDFS = dfs(pre)
                if not resultDFS:
                    return False
            seeing.remove(course)
            seen.add(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True


        