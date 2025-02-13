#problem link : https://leetcode.com/problems/search-a-2d-matrix/description/


class Solution:
    def isNumIn(self, m, t):
        left = 0
        right = len(m) - 1
        while left <= right:
            mid = (left + right) // 2
            if m[mid] == t:
                return True
            elif m[mid] < t:
                left = mid + 1
            else: 
                right = mid - 1
        return False





    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        colLen = len(matrix[0])
        for i in range(len(matrix)):
            if target<=matrix[i][colLen-1] and target>=matrix[i][0]:
                return self.isNumIn(matrix[i] , target)
        return False
        