class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        subset = []
        # If you choose to exclude, permanently excluded
        def solve(cur):
            if cur >= len(nums):
                ans.append(subset.copy())
                return
            
            subset.append(nums[cur])
            solve(cur+1)
            subset.pop()
            
            i = cur + 1
            while i < len(nums) and nums[i - 1] == nums[i]:
                i += 1
            solve(i)
        
        solve(0)
        return ans

        