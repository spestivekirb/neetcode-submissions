class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            tmp = (digits[i] + carry) // 10
            digits[i] = (digits[i] + carry) % 10
            carry = tmp
        
        if carry == 1:
            return [1] + digits
        else:
            return digits