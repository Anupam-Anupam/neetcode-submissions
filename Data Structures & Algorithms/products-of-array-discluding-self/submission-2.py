class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res1 = [1]
        mult1 = 1
        res2 = [1]
        mult2 = 1
        ans = []
        for x in range(0, len(nums)-1):
            mult1 *= nums[x]
            res1.append(mult1)
        for i in range(len(nums)-1, 0, -1):
            mult2 *= nums[i]
            res2.append(mult2)
        res2.reverse()
        for i in range(len(nums)):
            t = res1[i]*res2[i]
            ans.append(t)
        return ans



