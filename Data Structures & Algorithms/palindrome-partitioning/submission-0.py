class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Ok so at a new index, we add that to the currently being built one.
        # If the currently being built thing IS a palindrome, if so split
        # Regardless, run the continuation version
        ans = []
        partition = []
        substring = []
        def solve(index):
            nonlocal substring
            if index == len(s):
                if substring and substring == substring[::-1]:
                    partition.append("".join(substring))
                    ans.append(partition.copy())
                    partition.pop()
                return

            substring.append(s[index])

            if substring == substring[::-1]:
                state = substring.copy()
                partition.append("".join(substring))
                substring = []
                solve(index + 1)
                partition.pop()
                substring = state
            
            # Continue
            solve(index + 1)
            substring.pop()
        solve(0)

        return ans



                
