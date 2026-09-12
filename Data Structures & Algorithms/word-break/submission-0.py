class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Idea: If a split is possible somewhere we need to consider the split and non split routes.
        # We can figure out if a smaller thing is impossible on not if we've visited it previously.
        words = set(wordDict)

        memo = {}

        def solve(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in words:
                    if solve(j):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        

        return solve(0)