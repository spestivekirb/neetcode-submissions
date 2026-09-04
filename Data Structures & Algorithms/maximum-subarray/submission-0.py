class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        cursum = 0

        maxsum = -10001

        for n in nums:
            cursum += n
            maxsum = max(maxsum, cursum)

            while cursum < 0:
                cursum -= nums[left]
                left += 1
            
            
        

        return maxsum