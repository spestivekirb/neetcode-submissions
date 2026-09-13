class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # We basically need to find the final instance of the letter to make a substring.
        # If it is the only instance, we can just make it a string of size one.
        firstdict = {}
        lastdict = {}
        for i in range(len(s)):
            if s[i] not in firstdict:
                firstdict[s[i]] = i
            lastdict[s[i]] = i

        # New plan, two pointers. One at start, other will go to the end index but will update if one seen has a later end index.
        # When you reach end index, you can start a new substring.
        ans = []
        start = 0
        while start < len(s):  
            i = start
            end = lastdict[s[start]]
            while i <= end:
                end = max(end, lastdict[s[i]])
                i += 1
            ans.append(end - start + 1)
            start = end + 1
        return ans
