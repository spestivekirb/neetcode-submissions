class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        maxL = height[left]
        maxR = height[right]

        total_water = 0

        while left < right:
            if maxL < maxR:
                left += 1
                maxL = max(height[left], maxL)
                total_water += (maxL - height[left])
            else:
                right -= 1
                maxR = max(height[right], maxR)
                total_water += (maxR - height[right])
            
        return total_water





