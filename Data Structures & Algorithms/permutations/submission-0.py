class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Idea: We pick an index to swap to the front
        ans = []
        def swap(index1, index2):
            tmp = nums[index1]
            nums[index1] = nums[index2]
            nums[index2] = tmp
        def solve(selected):
            if selected == len(nums):
                ans.append(nums.copy())
            for i in range(selected, len(nums)):
                swap(selected, i)
                solve(selected + 1)
                swap(selected, i)
        solve(0)
        return ans

             
        