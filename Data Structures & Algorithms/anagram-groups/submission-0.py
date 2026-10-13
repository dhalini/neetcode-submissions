class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for i in strs:
            sort_strs = ''.join(sorted(i))
            dict[sort_strs].append(i)
            
        return list(dict.values())

        