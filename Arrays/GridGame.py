#problem link https://leetcode.com/problems/grid-game/

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        tSum  = sum(grid[0])
        bSum = 0
        ans = 9223372036854775807
        for i in range(len(grid[0])):
            tSum-=grid[0][i]
            temp = max(tSum , bSum)
            ans = min(ans , temp)
            bSum+=grid[1][i]
        return ans
            