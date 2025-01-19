#problem link : https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:        
        ans = []
            
        l =0
        r = len(matrix[0])
        t =0
        b = len(matrix)
        while(l<r and t<b):
            i =l
            for i in range(l, r):
                ans.append(matrix[t][i])
            t += 1
            for i in range(t , b):
                ans.append(matrix[i][r-1])
            r-=1
            if not (l < r and t < b):
                break
            for i in range(r - 1, l - 1, -1):
                ans.append(matrix[b - 1][i])
            b -= 1
            for i in range(b - 1, t - 1, -1):
                ans.append(matrix[i][l])
            l += 1
        return ans

        