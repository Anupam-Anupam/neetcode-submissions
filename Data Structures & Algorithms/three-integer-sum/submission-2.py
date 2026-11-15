class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()

        for i in range(len(nums)):
            left = 0 
            right = len(nums) - 1

            while left < right:
                if left == i:
                    left += 1
                    continue

                if right == i:
                    right -= 1
                    continue

                if nums[left] + nums[right] + nums[i] > 0:
                    right -= 1 
                
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1

                elif nums[left] + nums[right] + nums[i] == 0:
                    res.add(tuple(sorted((nums[left], nums[right], nums[i]))))
                    left += 1
                

        return [list(x) for x in res]

