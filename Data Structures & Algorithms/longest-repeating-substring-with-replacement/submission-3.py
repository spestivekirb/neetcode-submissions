class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        maxf = 0
        left = 0
        ans = 0
        for right in range(len(s)):
            count[ord(s[right])-ord("A")] += 1
            maxf = max(maxf, count[ord(s[right]) - ord("A")])
            
            while (right - left + 1) - maxf > k:
                count[ord(s[left]) - ord("A")] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans
        


        