#problem link : https://leetcode.com/problems/sort-array-by-parity/description/

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        k =0
        l = 0
        while(l<len(nums)):
            if(nums[l]%2==0):
                nums[k] , nums[l] = nums[l] , nums[k]
                k+=1
            l+=1
        return nums
        