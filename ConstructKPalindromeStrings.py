# problem link : https://leetcode.com/problems/construct-k-palindrome-strings/description/

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        b = set(s)
        odd= 0
        n = len(s)
        if(n<k):
             return (False)
        for i in b:
            if((s.count(i)%2!=0)):
                odd+=1
        if(odd<=k):
            return(True)
        else:
            return(False)
            
        