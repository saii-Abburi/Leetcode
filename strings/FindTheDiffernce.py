#problem Link : https://leetcode.com/problems/find-the-difference/description/?source=submission-noac

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for i in s+t:
            ans^= ord(i)
        return chr(ans)