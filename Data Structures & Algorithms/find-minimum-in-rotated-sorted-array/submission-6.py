class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]

        while (r - l) >= 1:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
               
        return nums[r]
            

            

        