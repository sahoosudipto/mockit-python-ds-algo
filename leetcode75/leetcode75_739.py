'''
739. Daily Temperatures
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

'''

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # ##stack implementation
        # answer = [0] * len(temperatures)
        # stack = []
        # for i, t in  enumerate(temperatures):
        #     # check which all previous days are colder compare to today
        #     # days present in stack means didn't find a hotter days yet
        #     while stack and temperatures[stack[-1]] < t:
        #         p_index = stack.pop()
        #         answer[p_index] = i - p_index
        #     stack.append(i)
        
        ## A DP approach
        # Iterate from the rightmost element -> last day(n-1)
        n = len(temperatures)
        answer = [0] * n
        for i in range(n - 2, -1, -1):
            next = i + 1
            while next < n: 
                if temperatures[next] > temperatures[i]:
                    answer[i] = next - i
                    break
                elif answer[next] == 0:
                    break
                next += answer[next]
        return answer
      
