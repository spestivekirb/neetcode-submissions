class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Idea -> pointer on word 1, pointer on word 2
        # Keep track of the two pointers and the edit distance.
        # If the word matches, we can just take it and increment both without distance (optimal)
        # Add ~ increment word 2 and edit distance
        # Replace ~ increment both words and edit distance
        # Delete ~ increment word 1 and edit distance.
        # Base case is when word 1 and word 2 are both at end, otherwise fail like idk 101 distance.

        memo = {}

        def solve(i1, i2):
            if i1 == len(word1) or i2 == len(word2):
                return max(abs(len(word1) - i1), abs(len(word2) - i2))
            if (i1, i2) in memo:
                return memo[(i1, i2)]
            

            if word1[i1] == word2[i2]:
                memo[(i1, i2)] = solve(i1 + 1, i2 + 1)
            else:
                memo[(i1, i2)] = 1 + min(
                    solve(i1, i2 + 1),  # Add
                    solve(i1 + 1, i2 + 1),  # Replace
                    solve(i1 + 1, i2) # Delete
                )

            return memo[(i1, i2)]
        
        return solve(0, 0)