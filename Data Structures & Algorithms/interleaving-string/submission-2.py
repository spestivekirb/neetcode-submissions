class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Ok so i guess we track the position of the array in s1 and s2, and we try to figure out of the remainder of s3 can be solved from that position?
        # Ohh ok we need to consider what if both pointer 1 and pointer 2 work in that pos.

        memo = {}

        def solve(i1, i2, i3):
            if i3 == len(s3):
                return i1 == len(s1) and i2 == len(s2)
            if i1 >= len(s1) and i2 >= len(s2):
                return False
            if (i1, i2) in memo:
                return memo[(i1, i2)]
            
            if i1 < len(s1) and i2 < len(s2):
                valid = False
                if s1[i1] == s3[i3]:
                    if solve(i1 + 1, i2, i3 + 1):
                        valid = True
                if s2[i2] == s3[i3]:
                    if solve(i1, i2 + 1, i3 + 1):
                        valid = True
                memo[(i1, i2)] = valid

            elif i1 == len(s1):
                if s2[i2] == s3[i3]:
                    memo[(i1, i2)] = solve(i1, i2 + 1, i3 + 1)
                else:
                    memo[(i1, i2)] = False
            
            else:
                if s1[i1] == s3[i3]:
                    memo[(i1, i2)] = solve(i1 + 1, i2, i3 + 1)
                else:
                    memo[(i1, i2)] = False
            
            return memo[i1, i2]
            
           
            

        return solve(0, 0, 0)
            
            