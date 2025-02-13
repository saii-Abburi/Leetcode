#problem link : https://leetcode.com/problems/maximum-ascending-subarray-sum/description/

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        temp = nums[0]
        for i in range(1,len(nums)):
            if(nums[i]>nums[i-1]):
                temp+=nums[i]
            else:
                temp = nums[i]
            ans = max(ans , temp)
        return ans