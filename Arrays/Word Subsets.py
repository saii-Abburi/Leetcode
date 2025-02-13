# problem link = https://leetcode.com/problems/word-subsets/description/


class Solution:

    def isSubset(self , word , word2):
        ans = dict()
        for i in word:
            if i not in ans:
                ans[i] =1
            else:
                ans[i]+=1
        for j in word2:
            if(j not in ans or(word2[j])>ans[j]):
                return False
        return True

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        d = {}
        for i in words2:
            for j in i:
                count=i.count(j)
                if j not in d or count>d[j]:
                    d[j]=count
        
        answer = [i for i in words1 if self.isSubset(i , d)]

        return answer
        
