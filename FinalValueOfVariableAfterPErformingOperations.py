#problem link : https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        s = ''.join(operations)
        plus = s.count('+')//2
        minus= s.count('-')//2
        return plus-minus