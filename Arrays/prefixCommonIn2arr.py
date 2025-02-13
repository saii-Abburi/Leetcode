#problem link : https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a , b = set() , set()
        count = 0
        res= []
        for i in range(len(A)):
            a.add(A[i])
            b.add(B[i])
            if(A[i]==B[i]):
                count+=1
            else:
                if B[i] in a:
                    count+=1
                if A[i] in b:
                    count+=1
            res.append(count)
        return res