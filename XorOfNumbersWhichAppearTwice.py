#problem link : https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/description/

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        d = {}
        res_list = []
        ans = 0
        for i in nums:
            if ( i not in d):
                d[i]=1
            else:
                d[i]+=1
        for key , value in d.items():
            if(value == 2):
                res_list.append(key)
        [ans := ans ^ i for i in res_list]  
        return ans
        