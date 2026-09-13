class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if (len(hand) % groupSize) != 0:
            return False
        freq = {}
        for card in hand:
            freq[card] = freq.get(card, 0) + 1
 
        hand.sort()
        
        for card in hand:
            if freq.get(card, 0) == 0:
                continue
            freq[card] -= 1
            for i in range(1, groupSize):
                if freq.get(card + i, 0) == 0:
                    return False
                else:
                    freq[card + i] -= 1
            
        return True
            


