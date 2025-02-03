#problem link : https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        temp =1
        for i in range(len(nums)-1):
            if(nums[i]<nums[i+1]):
                temp+=1
            else:
                temp =1
            ans = max(ans , temp)
        temp =1
        for i in range(len(nums)-1):
            if(nums[i]>nums[i+1]):
                temp+=1
            else:
                temp =1
            ans = max(ans , temp)

        return ans
