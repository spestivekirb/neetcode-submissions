class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        k = len(nums)
        ans = []
        for first in range(k - 2):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            
            second = first + 1
            third = k - 1

            while second < third:
                total = nums[first] + nums[second] + nums[third]
                if total == 0:
                    ans.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                    while second < third and nums[second] == nums[second - 1]:
                        second += 1
                    while second < third and nums[third] == nums[third + 1]:
                        third -= 1
                elif total < 0:
                    second += 1
                else:
                    third -= 1
            
        return ans
