#problem link : https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        ans = ""
        l = min(strs, key=lambda x: len(x))
        for i in range(len(l)):
            if(strs[0][i]== strs[len(strs)-1][i]):
                ans+=strs[0][i]
            else:
                break
        return ans