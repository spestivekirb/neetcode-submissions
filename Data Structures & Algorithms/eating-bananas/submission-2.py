import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while l < r:
            k = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            
            if hours <= h: # valid
                r = k
            else: #invalid
                l = k + 1
        return r
            