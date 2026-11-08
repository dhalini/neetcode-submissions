class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        ds = {}
        dt = {}
        cnt = 1
        for i in range(0,len(s)):
            ds[s[i]] = cnt + ds.get(s[i],0)
            dt[t[i]] = cnt + dt.get(t[i],0)
        for k in s:
            if(ds[k] != dt.get(k,0)):
                return False
        return True