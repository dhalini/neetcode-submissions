class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        seq_start = []
        max_count = 0
        for i in hash_set:
            if (i-1 not in hash_set):
                seq_start.append(i)
        for i in seq_start:
            count = 0
            while (i in hash_set):
                count = count + 1
                i = i+1
            max_count = max(max_count, count)
        return max_count

        