class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Any valid -> dfs? We go through the courses 
        # Topo sort

        edgemap = collections.defaultdict(list)
        indeg = [0] * numCourses
        ans = []

        for c, prq in prerequisites:
            edgemap[prq].append(c)
            indeg[c] += 1
        
        q = collections.deque()

        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        while q:
            cur = q.popleft()
            ans.append(cur)
            while edgemap[cur]:
                nxt = edgemap[cur].pop()
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)
        if len(ans) == numCourses:
            return ans
        else:
            return []