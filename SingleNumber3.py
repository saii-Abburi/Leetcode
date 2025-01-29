#problem link : https://leetcode.com/problems/single-number-iii/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dct = {}
        ans = []
        for i in nums:
            if(i in dct):
                dct[i]+=1
            else:
                dct[i]=1
        for key , value  in dct.items():
            if(value==1):
                ans.append(key)
        return ans 