class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edgedict = collections.defaultdict(list)
        for edge in times:
            edgedict[edge[0]].append((edge[1], edge[2]))

        distances = [float("inf")] * (n + 1)
        priority = [(0, k)]
        visited = set()

        while priority:
            curdist, curnode = heapq.heappop(priority)
            if curdist >= distances[curnode]:
                continue
            visited.add(curnode)
            
            distances[curnode] = curdist

            for neighbor in edgedict[curnode]:
                if neighbor[0] not in visited:
                    heapq.heappush(priority, (curdist + neighbor[1], neighbor[0]))
        
        if len(visited) != n:
            return -1
        else:
            return max(distances[1:])