#problem link : https://leetcode.com/contest/weekly-contest-433/problems/sum-of-variable-length-subarrays/?slug=maximum-and-minimum-sums-of-at-most-size-k-subsequences&region=global_v2

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            start = max(0 , i-nums[i])
            ans+= sum(nums[start:i+1])
        return ans