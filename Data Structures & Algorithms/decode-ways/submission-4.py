class Solution:
    def numDecodings(self, s: str) -> int:
        # Can try dp
        # dp [i] = ways to solve from index i onward
        # 0 ways to start starting with 0. 
        # If number is >= 3, its ways to solve i + 1
        # If number is 1, its ways to solve i+1 + ways to solve i + 2
        # If number is 2, depends on next number

        n = len(s)

        dp = [0] * (n + 1)
        if s[-1] != "0":
            dp[-2] = 1
        else:
            dp[-2] = 0
        dp[-1] = 1

        for i in range(n - 2, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            elif s[i] >= "3":
                dp[i] = dp[i+1]
            elif s[i] == "1":
                dp[i] = dp[i+1] + dp[i+2]
            else:
                if s[i+1] >= "7":
                    dp[i] = dp[i+1]
                else:
                    dp[i] = dp[i+1] + dp[i+2]
        return dp[0]