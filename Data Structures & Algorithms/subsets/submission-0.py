class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        subset = []

        def solve(index):
            if index >= len(nums):
                ans.append(subset.copy())
                return
            
            subset.append(nums[index])
            solve(index + 1)

            subset.pop()
            solve(index + 1)
        
        solve(0)
        return ans