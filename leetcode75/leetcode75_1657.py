# 1657. Determine if Two Strings Are Close

# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

# Example 1:

# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"

# Example 2:

# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa.


def closeStrings(word1: str, word2: str) -> bool:
  if set(word1) != set(word2):
    return False
  freq1 = sorted([word1.count(char) for char in set(word1)])
  freq2 = sorted([word2.count(char) for char in set(word2)])
  
  return freq1 == freq2

test1 = {"word1": "abc", "word2": "bca", "expected" : True}
test2 = {"word1": "cabbba", "word2": "abbccc", "expected" : True}
test3 = {"word1": "a", "word2": "aa", "expected" : False}
try:
  assert closeStrings(test1["word1"], test1["word2"]) == test1["expected"]
  print("test1 pass")
except AssertionError:
  print("Test case 1 failed")
try:
  assert closeStrings(test2["word1"], test2["word2"]) == test2["expected"]
  print("test2 pass")
except AssertionError:
  print("Test case 2 failed")
try:
  assert closeStrings(test3["word1"], test3["word2"]) == test3["expected"]
  print("test3 pass")
except AssertionError:
  print("Test case 3 failed")
