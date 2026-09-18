class Solution:
    
    def isHappy(self, n: int) -> bool:
        # Is there another way of determining if the number will reach 1?
        # Well the step before 1 must be like, a multiple of 10?
        seen = set()

        def solve(n):
            if n in seen:
                return False
            elif n == 1:
                return True

            seen.add(n)
            nextnum = 0
            while n:
                nextnum += (n%10)**2
                n //= 10
            return solve(nextnum)
        return solve(n)