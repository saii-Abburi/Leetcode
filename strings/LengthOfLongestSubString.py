#project link : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       l =0
       r =0
       if len(s)<=1:
         return len(s)
       max_count =1
       count  =1
       i= 0
       while(i<len(s)-1):
        if(s[r+1] not in s[l:r+1]):
            count+=1
            r+=1
            i+=1
        else:
            count-=1
            l+=1
        max_count = max(count , max_count)
       return max_count