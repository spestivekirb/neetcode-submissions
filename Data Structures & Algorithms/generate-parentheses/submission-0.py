class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Idea: keep track how how many paren pairs we have left
        ans = []
        trace = []
        def solve(rem, closed):
            if closed == n:
                ans.append("".join(trace))
                return
            elif rem == 0:
                trace.append(")")
                solve(rem, closed + 1)
                trace.pop()
            elif closed >= n - rem:
                trace.append("(")
                solve(rem - 1, closed)
                trace.pop()
            else:
                trace.append("(")
                solve(rem - 1, closed)
                trace.pop()
                trace.append(")")
                solve(rem, closed + 1)
                trace.pop()
        solve(n, 0)
        return ans

            
