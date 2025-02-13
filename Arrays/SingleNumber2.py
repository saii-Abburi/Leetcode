#problem Link : https://leetcode.com/problems/single-number-ii/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ct = {}
        for i in nums:
            if(i not in ct):
                ct[i]=1
            else:
                ct[i]+=1
        for key , value in ct.items():
            if(value==1):
                return key
        return -1