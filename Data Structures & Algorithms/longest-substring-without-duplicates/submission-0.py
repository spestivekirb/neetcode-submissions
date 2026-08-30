class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        seenSet = set()
        longest = 0
        while r < len(s):
            
            while s[r] in seenSet:
                seenSet.remove(s[l])
                l += 1
            
            seenSet.add(s[r])
            longest = max(longest, len(seenSet))
            r += 1

        return longest
        