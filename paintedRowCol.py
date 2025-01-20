# problem link : https://leetcode.com/problems/first-completely-painted-row-or-column/description/

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rLen, cLen = len(mat), len(mat[0])
        row, col = [0] * rLen, [0] * cLen
        ans = {}
        
        for i in range(rLen):
            for j in range(cLen):
                ans[mat[i][j]] = (i, j)
        
        for i, num in enumerate(arr):
            t_r, t_c = ans[num]
            row[t_r] += 1
            col[t_c] += 1
            
            if row[t_r] == cLen or col[t_c] == rLen:
                return i
        
        return -1
