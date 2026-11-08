class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res = res + str(len(i)) + "#" + i
        return res


    def decode(self, s: str) -> List[str]:
        l = []
        i = 0
        while (i<len(s)):
            j = i
            while (s[j]!='#'):
                j = j+1
            length = int(s[i:j])
            word = s[j+1:length+j+1]
            l.append(word)
            i = j+1+length
        return l