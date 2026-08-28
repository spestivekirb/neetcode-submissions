class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, tmp in enumerate(temperatures):
            while stack and tmp > stack[-1][0]:
                removedT, removedI = stack.pop()
                ans[removedI] = i - removedI
            stack.append([tmp, i])

        while stack:
            _, removedI = stack.pop()
            ans[removedI] = 0

        return ans