class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Idea: Start from end and find first index that can reach the end.
        # If something before that can reach the end, it could get there first.
        # If we get to the end of the array and we couldnt get to a prev index fail.

        cur = len(nums) - 1
        while cur >= 0:
            if cur == 0:
                return True
            prev = cur - 1
            while prev >= 0 and nums[prev] < cur - prev:
                prev -= 1
     
            cur = prev

        return False
        