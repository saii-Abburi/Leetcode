#problem link : https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        ans = []
        if(len(s1)!=len(s2)):
            return False
        for i in range(len(s1)):
            if(s1[i]!=s2[i]):
                ans.append(i)
        if(len(ans)==0):
            return True
        return (len(ans)==2) and (s1[ans[1]] == s2[ans[0]] and s1[ans[0]]== s2[ans[1]])