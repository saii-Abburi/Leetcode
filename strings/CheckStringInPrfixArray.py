#problem link : https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/description/

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        s2 = ""
        sL = len(s)
        for i in words:
            s2+=i
            if(sL>=len(s2) and s ==s2):
                return True
            elif(sL<len(s)):
                return False
        return False
            