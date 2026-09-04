class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        intervals.sort()
        curin = [intervals[0][0]]
        for i in range(1, len(intervals)):
            if intervals[i][1] < intervals[i-1][1]:
                intervals[i] = intervals[i-1]
            if intervals[i][0] > intervals[i-1][1]:
                curin.append(intervals[i-1][1])
                ans.append(curin)
                curin = [intervals[i][0]]

        curin.append(intervals[-1][1])   
        ans.append(curin)

        return ans