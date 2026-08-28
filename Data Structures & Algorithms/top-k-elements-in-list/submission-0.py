class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        for i in nums:
            if i in freqDict:
                freqDict[i] += 1
            else:
                freqDict[i] = 1
        revDict = {}
        for num in freqDict:
            freq = freqDict[num]
            if freq in revDict:
                revDict[freq].append(num)
            else:
                revDict[freq] = [num]
        
        keys = list(revDict.keys())
        keys.sort(reverse=True)
        
        ans = []
        for key in keys:
            ans.extend(revDict[key])
            if len(ans) >= k:
                break
        return ans
        

