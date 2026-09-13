class Solution:
    def checkValidString(self, s: str) -> bool:
        # Idea: We can store every ( and *. When we see a ), remove one ( or * if needed. 
        # At the end, both ( and * need to be 0


        lefts = []
        stars = []

        for i in range(len(s)):
            if s[i] == '(':
                lefts.append(i)
            elif s[i] == '*':
                stars.append(i)
            else:
                if lefts:
                    lefts.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        # Idea: Can match rightmost left with rightmost star atp if all are ( and *
        while lefts:
            if not stars:
                return False
            if lefts.pop() > stars.pop():
                return False
        return True