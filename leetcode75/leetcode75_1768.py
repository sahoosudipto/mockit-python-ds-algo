# -*- coding: utf-8 -*-
"""
#leetcode75- problem 1768: Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d

Constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""

def mergeAlternately( word1, word2):
    res = [ch[0] + ch[1] for ch in  zip(list(word1), list(word2))]
    if len(word1) > len(word2):
        res += list(word1)[len(word2):]
    else:
        res += list(word2)[len(word1):]
    print(''.join(res))

# word1 = "abcd"
# word2 = "pq"
# print(mergeAlternately(word1, word2))

def mergeAlternately_2(word1: str, word2: str) -> str:
    merge_str = ''
    for i in range(min(len(word1), len(word2))):
        merge_str += word1[i] + word2[i]
    merge_str += word1[i+1:] if len(word1) > len(word2) else word2[i+1:]
    return merge_str


# word1 = "abcd"
# word2 = "pq"
# # print(mergeAlternately_2(word1, word2))
