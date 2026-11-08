class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(0,len(nums)+1)]
        l=[]
        for i in nums:
            count[i] = 1 + count.get(i,0)
        for key,value in count.items():
            freq[value].append(key)
        for j in range(len(freq)-1,0,-1):
            for num in freq[j]:
                l.append(num)
            if(len(l) == k):
                return l

      
 
            

        