#problem link : https://leetcode.com/problems/buddy-strings/description/

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal:
            # If the strings are identical, check if there are any duplicate characters
            return len(set(s)) < len(s)
        
        mismatched_indices = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                mismatched_indices.append(i)
                if len(mismatched_indices) > 2:
                    return False
        
        # If there are exactly two mismatched characters, check if swapping them makes the strings equal
        return len(mismatched_indices) == 2 and s[mismatched_indices[0]] == goal[mismatched_indices[1]] and s[mismatched_indices[1]] == goal[mismatched_indices[0]]