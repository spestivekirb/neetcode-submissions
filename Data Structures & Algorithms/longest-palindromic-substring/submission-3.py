class Solution:
    def longestPalindrome(self, s: str) -> str:
        # I guess the sort of dp is that we check that that two chars are the same and anything between them is a palindrome.
        # Complete-ish search so tab faster
        longest = ""

        for i in range(len(s)): # Odd lens
            left = right = i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left + 1 > len(longest):
                        longest = s[left:right+1]
                    left -= 1
                    right += 1
                else:
                    break
        

        for i in range(len(s) - 1): # Even lens
            left = i
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left + 1 > len(longest):
                        longest = s[left:right+1]
                    left -= 1
                    right += 1
                else:
                    break
        return longest
