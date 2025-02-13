#problem link : https://leetcode.com/problems/tuple-with-same-product/

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        temp_dict ={}
        count  =0
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                num =  nums[i]*nums[j]
                if num not in temp_dict:
                    temp_dict[num]= 1
                else:
                    temp_dict[num]+=1
        for i in temp_dict.values():
            if i>1:
                count+= 8*(i*(i-1)//2)
        return count