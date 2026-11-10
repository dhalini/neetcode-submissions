class Solution:
    def isPalindrome(self, s: str) -> bool:
        res1 = ""
        res2 = ""
        for c in range(len(s)-1, -1, -1):
            if(s[c].isalnum()):
                res1+=s[c]
        for c in range(0,len(s)):
            if(s[c].isalnum()):
                res2+=s[c]
        #print(res.lower())
        if(res1.lower()==res2.lower()):
            return True
        return False
        