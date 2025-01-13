#problem link : https://leetcode.com/problems/minimum-length-of-string-after-operations/

class Solution:
    def minimumLength(self, s: str) -> int:
        s_set = set(s)
        ans = 0
        for i in s_set:
            c = s.count(i)
            if(c%2):
                ans+=1
            else:
                ans+=2
        return ans