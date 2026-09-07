class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Idea: Since order does not matter, we can basically choose to:
        # a) Pick the same num again
        # b) Do not pick the num again, move to next.
        ans = []
        trace = []
        def solve(index, sum):
            if sum > target:
                return
            if sum == target:
                ans.append(trace.copy())
                return
            if index >= len(nums):
                return
            
            trace.append(nums[index])
            solve(index, sum + nums[index])

            trace.pop()
            solve(index + 1, sum)
        
        solve(0, 0)
        return ans