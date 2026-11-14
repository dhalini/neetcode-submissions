class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        hashmap = {}
        res = []
        for i in nums:
            count[i] = 1 + count.get(i,0)
        for i in range(0,len(nums)+1):
            hashmap[i] = []
        for key, value in count.items():
            hashmap[value].append(key)
        for i in range(len(hashmap)-1, 0, -1):
            for num in hashmap[i]:
                res.append(num)
                if (len(res)==k):
                    return res
        
            

        