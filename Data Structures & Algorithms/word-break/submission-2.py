class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        n = len(s)
        # Idea: we just figure out if we can solve it from an index onward

        def solve(index):
            if index >= n:
                return True

            if index in memo:
                return memo[index]
            
            for word in wordDict:
                l = len(word)
                if n - index >= l and s[index:index+l] == word:
                    if index not in memo or not memo[index]:
                        memo[index] = solve(index+l)
            
            if index not in memo:
                memo[index] = False


            return memo[index]
        
        return solve(0)