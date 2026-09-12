class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Seperate segments with '0'
        prefix = suffix = 0
        ans = nums[0]

        for i in range(len(nums)):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[len(nums) - i - 1] * (suffix or 1)
            ans = max(ans, prefix, suffix)

        return ans