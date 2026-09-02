class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # idea -> we can determine if l is sorted or not and based on that figure out which side to look.

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            print(l, r, m)
            if nums[m] == target:
                return m
            elif nums[m] >= nums[l]: # If left sorted
                if nums[m] > target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:   # If right sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
        
        return -1
