class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashtable = [0] * 26

        movinghash = [0] * 26

        for c in s1:
            hashtable[ord(c) - ord('a')] += 1
        if len(s2) < len(s1):
            return False

        l = 0
        for r in range(len(s2)):
            movinghash[ord(s2[r]) - ord('a')] += 1
            while r - l + 1 > len(s1):
                movinghash[ord(s2[l]) - ord('a')] -= 1
                l += 1

            r += 1
            if hashtable == movinghash:
                return True
        
        return False