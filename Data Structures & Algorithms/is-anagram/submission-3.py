class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = {}
        t1 = {}
        
        for i in s:
            if i in s1:
                s1[i] = s1[i] + 1
            #s1.add(i)
            #s1c = s1c+1
            else:
                s1[i] = 1
        for j in t:
            if j in t1:
                
                t1[j] = t1[j] + 1

            #t1.add(j)
            #t1c=t1c+1
            else:
                t1[j] = 1
        if(s1==t1):
            return True
        return False

        