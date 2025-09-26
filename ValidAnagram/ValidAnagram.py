"""Given two strings s and t, return true if the two strings
are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another 
string, but the order of the characters can be different.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic.update({s[i]:1})
    
        for i in range(len(t)):
            if t[i] in dic:
                dic[t[i]] -= 1
            else: 
                return False
            
        return all(value == 0 for value in dic.values())
