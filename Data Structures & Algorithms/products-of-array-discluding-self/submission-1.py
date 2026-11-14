class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_num = [0] * len(nums)
        prefix = 1
        postfix = 1
        res = [0] * len(nums)
        for i in range(0,len(nums)):
            pre_num[i] = prefix
            prefix = prefix * nums[i]
        for i in range(len(nums)-1, -1, -1):
            res[i] = postfix * pre_num[i]
            postfix = postfix * nums[i]
        return res