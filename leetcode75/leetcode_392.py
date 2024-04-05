'''
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
'''

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if  not s:
            return True
        elif len(s) > len(t):
            return False
        # s = list(s)
        # t = list(t)
        # i, j = 0, 0
        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         i += 1
        #     j += 1
        # if i == len(s):
        #     return True
        # else:
        #     return False

        ####with FInd
        # index = 0
        # count = 0 
        # while count < len(s):
        #     i = t[index:].find(s[count])
        #     if i == -1:
        #         return False
        #     else:
        #         count += 1
        #     index += i + 1
        # return True

        ###for each
        count = 0
        for ch in t:
            if count == len(s):
                return True
            if ch == s[count]:
                count += 1
        if count == len(s):
            return True
        else: 
            return False
