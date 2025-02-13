#problem link : https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
class Solution:
    def check(self, nums: List[int]) -> bool:
        b = sorted(nums)
        k =0
        for i in range(len(nums)-1):
            if(nums[i]>nums[i+1]):
                k =i+1
                break
        b = b[-k:]+b[:-k]
        return b  == nums
