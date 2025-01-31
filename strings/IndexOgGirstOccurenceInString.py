#probelm link : https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h1 = len(haystack)
        n1 = len(needle)
        if n1>h1:
            return -1
        
        for i in range(0 , h1-n1+1):
            if(haystack[i:i+n1]==needle):
                return i
        return -1