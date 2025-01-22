#problem link : https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description/

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sList = sentence.split(" ")
        for i, word in enumerate(sList, 1):
            if(word.startswith(searchWord)):
                return i
        return -1

        