class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {")": "(", "]": "[", "}": "{"}
        stack = []
        for bracket in s:
            if bracket in bracketMap:
                if stack and stack[-1] == bracketMap[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        if stack:
            return False
        else:
            return True