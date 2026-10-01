class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        # Odds
        for i in range(n):
            left = right = i
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break
        
        # Evens
        for i in range(n-1):
            left = i
            right = i + 1
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break
        return count