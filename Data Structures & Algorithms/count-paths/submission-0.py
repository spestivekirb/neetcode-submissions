
class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        # Answer is just m - 1 choose m + n - 2
        # n C r is n! / r! (n-r)!
        return (math.factorial(m + n - 2))//((math.factorial(m - 1) * math.factorial(n-1)))