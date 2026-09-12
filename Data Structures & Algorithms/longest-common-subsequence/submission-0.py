class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Well an increasing subsequence must extend from a previous one.
        # So at a given index for each, if the are equal we can add 1 to longest
        # I guess memo the lis from that index onward

        memo = {}

        def solve(in1, in2):
            if in1 >= len(text1) or in2 >= len(text2):
                return 0
            if (in1, in2) in memo:
                return memo[(in1, in2)]
            if text1[in1] == text2[in2]:
                memo[(in1, in2)] = 1 + solve(in1 + 1, in2 + 1)     
            else:
                memo[(in1, in2)] = max(solve(in1 + 1, in2), solve(in1, in2 + 1))
            return memo[(in1, in2)]

        return solve(0, 0)