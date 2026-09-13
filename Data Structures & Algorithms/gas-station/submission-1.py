class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        
        # ok so like we basically see if our sum can make it, if not just restart.
        # if gas >= cost then we can guarantee that the one that makes it to the final gas station can fully loop.
        
        start = 0
        total = gas[start]
        for end in range(1, len(gas)):
            if total < cost[end - 1]:
                total = gas[end]
                start = end
            else:
                total -= cost[end - 1]
                total += gas[end]
        
        return start

