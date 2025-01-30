#problem link :https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        s1 = ''.join(sorted(s1))
        for i in range(len(s2)):
             if s1 == "".join(sorted(s2[i:i+k])): 
                return True
        return False
        