class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i in range(0,len(nums)):
            res = target - nums[i]
            if (res in hashset and i!=hashset[res]):
                return [hashset[res],i]
            hashset[nums[i]] = i

        