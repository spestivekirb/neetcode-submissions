"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Greedy could be like, number of overlapping? 
        # Maybe we keep a queue of current meetings? Sort by earliest end time.
        # I guess we have a master time object? That loops through to max      
        minRooms = 0
        intervals.sort(key = lambda interval : interval.start)
    
        minheap = []
        
        
        for meeting in intervals:
            while minheap and minheap[0] <= meeting.start:
                heapq.heappop(minheap)
            heapq.heappush(minheap, meeting.end)
            minRooms = max(minRooms, len(minheap))

        return minRooms