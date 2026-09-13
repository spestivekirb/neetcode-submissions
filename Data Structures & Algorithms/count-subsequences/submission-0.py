class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # We need to store the current index of s and current index of t.
        # We need to compute the number of ways to form the rest of t from s.
        # If a number matches, we need to consider not taking it AND taking it, otherwise dont take.

        memo = {}

        def solve(si, ti):
            if ti >= len(t):
                return 1
            if si >= len(s):
                return 0
            
            if (si, ti) in memo:
                return memo[(si, ti)]
            
            if s[si] == t[ti]:
                memo[(si, ti)] = solve(si + 1, ti + 1) + solve(si + 1, ti)
            else:
                memo[(si, ti)] = solve(si + 1, ti)

            return memo[(si, ti)]
        
        return solve(0, 0)