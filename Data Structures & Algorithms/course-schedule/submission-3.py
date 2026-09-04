class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        prereqdict = collections.defaultdict(list)
        for edge in prerequisites:
            prereqdict[edge[0]].append(edge[1])
        def checkPrereq(course, coursepath):
            if course in visited:
                return True
            if course not in prereqdict:
                return True
            if course in coursepath:
                return False
            for prereq in prereqdict[course]:
                coursepath.add(course)
                if not checkPrereq(prereq, coursepath):
                    return False
            coursepath.remove(course)


            return True

        for course in prereqdict:
            if not checkPrereq(course, set()):
                return False
            visited.add(course)
        return True



