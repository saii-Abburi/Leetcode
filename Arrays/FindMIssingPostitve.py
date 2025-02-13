#problem link : https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        temp =[0]*(n+1)
        for i in nums:
            if(1<=i<=n):
                temp[i-1]+=1
        for i in range(n):
            if(temp[i]==0):
                return i+1
        return n+1