#problem link : https://leetcode.com/problems/concatenation-of-array/description/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans =[]
        ans.extend(nums)
        ans.extend(nums)
        return ans