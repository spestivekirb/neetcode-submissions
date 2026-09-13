class Solution:
    def jump(self, nums: List[int]) -> int:
        # What could the greedy assumption be? 
        # Ok well we need to find the first element from the right

        # Well it makes sense to take the furthest distance in range, but maybe like
        # We consider jumplen + dist to pick the optimal.
        if len(nums) == 1:
            return 0

        jumps = 0
        i = 0
        while True:
            if nums[i] + i >= len(nums) - 1:
                return 1 + jumps
            possible = nums[i+1:i + nums[i] + 1]
            for j in range(nums[i]):
                possible[j] += (j + 1)
            
            jumps += 1
            i = i + 1 + possible.index(max(possible))
        
