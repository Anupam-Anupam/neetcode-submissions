class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        nums = sorted(nums)

        left = 0
        right = left + 1

        while right < len(nums):
            if nums[left] < nums[right]:
                left += 1
                right += 1

            elif nums[left] == nums[right]:
                return nums[left]

        return None 