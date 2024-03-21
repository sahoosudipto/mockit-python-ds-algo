"""leetcode75_1071
#1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""
def greatest_common_divisor_of_strings(str1: str, str2: str) -> str:
  # Handle empty strings
  if not str1 or not str2:
    return ""
  # Get the length of the shorter string
  n = min(len(str1), len(str2))

  # Iterate through divisors (potential GCD lengths)
  for divisor in range(n, 0, -1):
    # Check if the divisor divides both strings
    if all(str1[i:i + divisor] == str1[:divisor] for i in range(0, len(str1), divisor)) and \
       all(str2[i:i + divisor] == str1[:divisor] for i in range(0, len(str2), divisor)):
        return str1[:divisor]  # Both strings are divisible by the divisor

  return ""


def gcd_of_strings(str1: str, str2: str) -> str:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    if(str1 == str2):
        return str1
    if str1 + str2 != str2 + str1:
        return ""

    divisor_length = gcd(len(str1), len(str2))
    return str1[:divisor_length]

str1 = "ABABABABABABABABABABABAB"
str2 = "ABABABABABABABAB"
gcd_of_strings(str1, str2)

str1 = "LEET"
str2 = "CODE"
greatest_common_divisor_of_strings(str1, str2)
