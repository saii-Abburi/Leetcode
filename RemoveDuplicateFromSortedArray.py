#problem link : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        j = 2 
        for i in range(2, len(nums)):
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
                
        return j