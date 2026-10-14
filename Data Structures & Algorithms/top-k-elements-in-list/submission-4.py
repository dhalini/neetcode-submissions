class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashset = Counter(nums)
        l=[]
        #for i in nums:
            #hashset[i] = nums.count(i)
        bucket = [[]for i in range(0,len(nums)+1)]
        for num, freq in hashset.items():
            bucket[freq].append(num)
        for j in range (len(bucket)-1, 0, -1):
            for n in bucket[j]:
                l.append(n)
            if (len(l)==k):
                return l
 
            

        