class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashDict = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c)-ord("a")] += 1
            
            tcount = tuple(count)
            if tcount in hashDict:
                hashDict[tcount].append(word)
            else:
                hashDict[tcount] = [word]
        
        return list(hashDict.values())