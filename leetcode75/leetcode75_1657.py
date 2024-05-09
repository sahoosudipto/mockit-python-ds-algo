{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNSyaz29tUHyBLwzyxotair",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sahoosudipto/mockit-python-ds-algo/blob/main/leetcode75/leetcode75_1657.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 22,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zsLXT4Hkzklw",
        "outputId": "9350c342-c3ee-4b51-d1c3-c1a36f892e60"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Test case 1 failed\n",
            "test2 pass\n",
            "test3 pass\n"
          ]
        }
      ],
      "source": [
        "# 1657. Determine if Two Strings Are Close\n",
        "\n",
        "# Two strings are considered close if you can attain one from the other using the following operations:\n",
        "\n",
        "# Operation 1: Swap any two existing characters.\n",
        "# For example, abcde -> aecdb\n",
        "# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.\n",
        "# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)\n",
        "# You can use the operations on either string as many times as necessary.\n",
        "\n",
        "# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.\n",
        "\n",
        "\n",
        "\n",
        "# Example 1:\n",
        "\n",
        "# Input: word1 = \"abc\", word2 = \"bca\"\n",
        "# Output: true\n",
        "# Explanation: You can attain word2 from word1 in 2 operations.\n",
        "# Apply Operation 1: \"abc\" -> \"acb\"\n",
        "# Apply Operation 1: \"acb\" -> \"bca\"\n",
        "\n",
        "# Example 2:\n",
        "\n",
        "# Input: word1 = \"a\", word2 = \"aa\"\n",
        "# Output: false\n",
        "# Explanation: It is impossible to attain word2 from word1, or vice versa.\n",
        "\n",
        "\n",
        "def closeStrings(word1: str, word2: str) -> bool:\n",
        "  if set(word1) != set(word2):\n",
        "    return False\n",
        "  freq1 = sorted([word1.count(char) for char in set(word1)])\n",
        "  freq2 = sorted([word2.count(char) for char in set(word2)])\n",
        "\n",
        "  return freq1 == freq2\n",
        "\n",
        "test1 = {\"word1\": \"abc\", \"word2\": \"bca\", \"expected\" : True}\n",
        "test2 = {\"word1\": \"cabbba\", \"word2\": \"abbccc\", \"expected\" : True}\n",
        "test3 = {\"word1\": \"a\", \"word2\": \"aa\", \"expected\" : False}\n",
        "try:\n",
        "  assert closeStrings(test1[\"word1\"], test1[\"word2\"]) == test1[\"expected\"]\n",
        "  print(\"test1 pass\")\n",
        "except AssertionError:\n",
        "  print(\"Test case 1 failed\")\n",
        "try:\n",
        "  assert closeStrings(test2[\"word1\"], test2[\"word2\"]) == test2[\"expected\"]\n",
        "  print(\"test2 pass\")\n",
        "except AssertionError:\n",
        "  print(\"Test case 2 failed\")\n",
        "try:\n",
        "  assert closeStrings(test3[\"word1\"], test3[\"word2\"]) == test3[\"expected\"]\n",
        "  print(\"test3 pass\")\n",
        "except AssertionError:\n",
        "  print(\"Test case 3 failed\")\n",
        "\n",
        "\n",
        "\n"
      ]
    }
  ]
}