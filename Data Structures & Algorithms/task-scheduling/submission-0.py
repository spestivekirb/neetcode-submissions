class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cooldown = collections.deque()
        taskfreq = collections.defaultdict(int)
        for task in tasks:
            taskfreq[task] += 1
        
        maxheap = [(-taskfreq[task], task) for task in taskfreq]
        heapq.heapify(maxheap)
        cycles = 0

        while maxheap or cooldown:
            cycles += 1
            if maxheap:
                task = heapq.heappop(maxheap)
                remaining = task[0] + 1
                
                if remaining < 0:
                    cooldown.append((remaining, task[1], cycles + n))
            
            
            if cooldown and cooldown[0][2] <= cycles:
                heapq.heappush(maxheap, (cooldown[0][0], cooldown[0][1]))
                cooldown.popleft()
        
        return cycles


            


        
        return cycles