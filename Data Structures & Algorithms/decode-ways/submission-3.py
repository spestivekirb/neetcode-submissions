class Solution:
    def numDecodings(self, s: str) -> int:
        # If next num 0, must be combinde with 1 or 2.
        # If first num is 1 -> pick or combine w next.
        # If first num is 2, either pick or comb with next (IF 1-6)
        # Otherwise just take the num.
        if s == "0":
            return 0
        memo = [-1] * (len(s) + 1)
        def solve(index):
            if memo[index] != -1:
                return memo[index]
            if index >= len(s) - 1:
                return 1
            if s[index] == "0":
                memo[index] = 0
                return 0
            elif s[index] == "1":
                if s[index + 1] == "0":
                    memo[index] = solve(index + 2)
                else:
                    memo[index] = solve(index + 1) + solve(index + 2)
            elif s[index] == "2":
                if "1" <= s[index + 1] <= "6":
                    memo[index] = solve(index + 1) + solve(index + 2) 
                elif s[index + 1] == "0":
                    memo[index] = solve(index + 2)
                else:
                    memo[index] = solve(index + 1)
            else:
                memo[index] = solve(index + 1)
            return memo[index]

        return solve(0)

