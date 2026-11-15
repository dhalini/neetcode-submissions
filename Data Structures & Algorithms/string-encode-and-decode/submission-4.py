class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            res += str(len(i)) + '#' + i
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while (i <len(s)):
            j = i
            while(s[j]!='#'):
                j=j+1
            l = int(s[i:j])
            word = s[j+1:l+j+1]
            res.append(word) 
            i = j+l+1
        return res       