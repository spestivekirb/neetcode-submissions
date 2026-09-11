class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x *= -1
        else:
            sign = 1
        rev = 0
        while x:
            rev *= 10
            rev += x % 10
            x //= 10
        
        return rev * sign if rev < (1 << 31) else 0

