class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def solve(i, cursum, trace):
            if cursum > target:
                return
            if cursum == target:
                ans.append(trace.copy())
                return
            if i >= len(candidates):
                return
            
            trace.append(candidates[i])
            solve(i+1, cursum + candidates[i], trace)
            trace.pop()
            j = i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            solve(j, cursum, trace)
        solve(0, 0, [])
        return ans