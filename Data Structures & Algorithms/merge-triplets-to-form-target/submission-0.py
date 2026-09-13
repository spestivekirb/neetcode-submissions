class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Ok so i think we can just go through all the triplets.
        # If every value in the triplet is <= the target, we can add it.
        maxSeen = [0] * 3
        for triplet in triplets:
            valid = True
            for i in range(3):
                if triplet[i] > target[i]:
                    valid = False
            if valid:
                for j in range(3):
                    maxSeen[j] = max(maxSeen[j], triplet[j])
        
        return maxSeen == target
