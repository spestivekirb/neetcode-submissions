class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Memo idea: Keep the length of the max inc subsequence starting from pos
        if len(nums) == 1:
            return 1

        memo = [0] * len(nums)
        def solve(start):
            if memo[start] != 0:
                return memo[start]

            if start == len(nums) - 1:
                memo[start] = 1
                return 1
            
            maxSeen = 0
            for end in range(start + 1, len(nums)):
                if nums[start] < nums[end]:
                    maxSeen = max(maxSeen, solve(end))
            memo[start] = 1 + maxSeen
            return 1 + maxSeen
        
        for i in range(len(nums)):
            if memo[i] == 0:
                solve(i)
        return max(memo)


        