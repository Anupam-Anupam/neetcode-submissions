class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## naively, we can multiply all the elements of the list, then append a new list in which each indexed element = the product divided by the indexed element in the original list
        prefix = [1]*(len(nums)+1)
        suffix = [1]*(len(nums)+1)
        res = [1]*len(nums)

        for i in range(len(nums)):
            prefix[i+1] = prefix[i]*nums[i]

        for i in range(len(nums)-1, 0, -1):
            suffix[i-1] = suffix[i] * nums[i]

        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]


        return res
