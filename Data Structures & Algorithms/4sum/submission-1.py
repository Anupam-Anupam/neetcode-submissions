class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = set()
        nums = sorted(nums)
        result = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                left, right = 0, len(nums) - 1
                targ = target - (nums[i] + nums[j])


                while left < right:

                    if left == i or left == j:
                        left += 1
                        continue

                    elif right == i or right == j:
                        right -= 1
                        continue

                    elif nums[left] + nums[right] > targ:
                        right -= 1

                    elif nums[left] + nums[right] < targ:
                        left += 1

                    elif nums[left] + nums[right] == targ:
                        res.add(tuple(sorted((nums[i], nums[j], nums[left], nums[right]))))
                        left += 1
                        right -= 1
            

        return [list(quad) for quad in res]
         



