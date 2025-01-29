#problem link : https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        rev = int(str(abs(x))[::-1]) * (1 if x>0 else -1)
        if rev < -2147483648 or rev > 2147483647:
            return 0
        return rev