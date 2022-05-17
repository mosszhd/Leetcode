class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = dict()
        sum = 0
        if(len(s)!=len(t)):
            return False
        for i in s:
            if i not in count1:
                count1[i] = 1
            else:
                count1[i] += 1
        for i in t:
            if i not in count1:
                return False
            else:
                count1[i] -=1
        
        for i in count1:
            if count1[i] != 0:
                return False
            else:
                return True
