#problem link : https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count =0
        for i in range(left , right+1):
          word = words[i]
          if (word[0] in 'aeiouAEIOU' and word[-1] in 'aeiouAEIOU'):
            count+=1
        return count