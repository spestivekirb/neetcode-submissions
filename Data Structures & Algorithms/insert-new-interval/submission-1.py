class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Ok so basically, we need to insert according to start, but then look at adjacent ones
        # Removal is an O(n) operation which is not good!
        # But we could just add anything to the array if the end index less than interval.

        res = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        if i == len(intervals):
            res.append(newInterval)
            return res
        newStart = min(newInterval[0], intervals[i][0])
        newEnd = newInterval[1]
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newEnd = max(newEnd, intervals[i][1])
            i += 1
        res.append([newStart, newEnd])
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res