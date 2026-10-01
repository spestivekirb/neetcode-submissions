class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]
        
        dp1 = [0] * n
        dp2 = [0] * n
        dp1[0] = nums[0]

        for i in range(1, n):
            dp1[i] = max(nums[i] + dp1[i-2], dp1[i-1])
            dp2[i] = max(nums[i] + dp2[i-2], dp2[i-1])
        return max(dp1[-2], dp2[-1])
        