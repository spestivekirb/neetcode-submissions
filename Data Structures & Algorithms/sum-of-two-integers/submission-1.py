class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 2 + 3 -> 5
        # 010 + 011 -> 101
        # If carry 0, Sum is a xor b, carry is a and b
        # If carry 1 -> a xor b xor carry is digit,
        # New carry is a or b?
        def calculate(a, b, carry):
            if carry:
                return a ^ b ^ 1, a | b
            else:
                return a ^ b, a & b
        
        ans = 0
        carry = 0
        for i in range(32):
            if not a and not b and not carry:
                return ans
            
            s, carry = calculate(a & 1, b & 1, carry)
            a >>= 1
            b >>= 1
            s <<= i
            ans |= s
        return ans if ans < (1 << 31) else ~(ans ^ 0xFFFFFFFF)
