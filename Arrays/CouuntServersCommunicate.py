#problem link :https://leetcode.com/problems/count-servers-that-communicate/description/


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        total_servers = 0
        single_servers =0
        m = len(grid)
        n = len(grid[0])
        row = [0]*m
        col = [0]*n
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    row[i]+=1
                    col[j]+=1
                    total_servers+=1
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1 and (row[i]<=1 and col[j]<=1)):
                    single_servers+=1
        return total_servers - single_servers

