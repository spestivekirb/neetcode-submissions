class Solution:
    def reverseBits(self, n: int) -> int:
        # 6: 0...110 -> -6 = 1...010 -> 1...101
        # 3: 0...011 -> -3 = 1...101
        # 19: 0...10011 -> -19 = 1...01101 -> 
        # 25: 0...11001 -> -25 = 1...00111


        ans = 0
        for i in range(32):
            ans <<= 1
            ans += (n & 1)
            n >>= 1
        return ans