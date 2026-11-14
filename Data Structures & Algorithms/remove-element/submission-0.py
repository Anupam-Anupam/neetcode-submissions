class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = -1

        nums.sort(reverse = True)
        k = 0
        for num in nums:
            if num > -1:
                k += 1

        return k
            