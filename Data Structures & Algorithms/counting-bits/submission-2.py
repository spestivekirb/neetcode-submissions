class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0 -> 0
        # 1 -> 1 -> offset 1?
        # 10 -> 1 -> offset 2
        # 11 -> 2
        # 100 -> 1 -> offset 4
        # 101 -> 2
        # 110 -> 2
        # 111 -> 3
        # 1000 -> 1 -> offset 8
        ans = [0] * (n + 1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset *= 2
            ans[i] = 1 + ans[i - offset]
            

            
        return ans

