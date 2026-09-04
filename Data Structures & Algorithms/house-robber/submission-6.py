class Solution:
    def rob(self, nums: List[int]) -> int:
        # Idea: We either do ideal from robbing house n - 2 and this house or ideal from robbing house n - 1.

        dp = []

        for i in range(len(nums)):
            if i == 0:
                dp.append(nums[0])
            elif i == 1:
                dp.append(max(nums[0], nums[1]))
            else:
                dp.append(max(nums[i] + dp[i-2], dp[i-1]))
        
        return dp[-1]

        