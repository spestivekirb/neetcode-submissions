class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0 -> 0
        # 1 -> 1
        # 10 -> 1 -> 1 + 2 pos before
        # 11 -> 2
        # 100 -> 1 -> 1 + 4 pos before
        # 101 -> 2
        # 110 -> 2
        # 111 -> 3
        # 1000 -> 1 -> 1 + 8 pos before?
        if n == 0:
            return [0]
        ans = [0] * (n + 1)
        ans[1] = 1
        offset = 1

        for i in range(2, n+1):
            
            ans[i] = 1 + ans[i - 2**offset]
            if 2 ** (offset + 1) == i + 1:
                offset += 1
            
        return ans

