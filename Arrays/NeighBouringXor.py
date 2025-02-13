#problem Link : https://leetcode.com/problems/neighboring-bitwise-xor/

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        result = 0
        [result := result ^ x for x in derived]
        if(result):
            return False
        else:
            return True