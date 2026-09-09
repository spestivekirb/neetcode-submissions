class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []
        ans = []
        cur = []

        letterdict = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"

        }
        def solve(index):
            if index == len(digits):
                ans.append("".join(cur))
                return
            for c in letterdict[int(digits[index])]:
                cur.append(c)
                solve(index + 1)
                cur.pop()
        solve(0)
        return ans
            
            

        