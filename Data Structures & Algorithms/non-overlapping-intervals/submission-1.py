class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # I guess if there are multiple overlapping intervals we should just remove the one with the latest end? 
        # We sort by end, and I guess we just count the number of invalids to add on?
        reverse = [[interval[1], interval[0]] for interval in intervals]
        reverse.sort()
        lastEnd = float("-inf")
        deletions = 0
        for interval in reverse:
            if interval[1] < lastEnd:
                deletions += 1
            else:
                lastEnd = interval[0]
        
        return deletions
