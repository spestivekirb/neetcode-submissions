class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefix[0] = nums[0]
                suffix[-1] = nums[-1]
            else:
                prefix[i] = prefix[i-1] * nums[i]
                suffix[len(nums) - i - 1] = suffix[len(nums) - i] * nums[len(nums) - i - 1]

        ans = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                ans[0] = suffix[1]
            elif i == len(nums) - 1:
                ans[len(nums) - 1] = prefix[-2]
            else:
                ans[i] = prefix[i-1] * suffix[i+1]
        return ans