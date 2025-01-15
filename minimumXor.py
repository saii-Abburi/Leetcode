#problem link : https://leetcode.com/problems/minimize-xor/description/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        c1 = bin(num1).count('1')
        c2 = bin(num2).count('1')

        if c1 == c2:
            return num1


        if c1 < c2:
            diff = c2 - c1
            num = num1
            for i in range(32):
                if not (num1 & (1 << i)):
                    num |= (1 << i)
                    diff -= 1
                    if diff == 0:
                        break
            return num

        if c1 > c2:
            diff = c1 - c2
            num = num1
            for i in range(32):
                if num1 & (1 << i):
                    num &= ~(1 << i)
                    diff -= 1
                    if diff == 0:
                        break
            return num
