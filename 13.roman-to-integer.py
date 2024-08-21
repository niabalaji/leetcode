#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # create a dictionary in python to map the values
        roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        # if the value of the current numeral is less 
        # than the value of the next numeral we 
        # subtract the value of the current numeral 
        # from the next
        # otherwise we keep adding the values to 
        # a counter 
        count = 0 
        length = len(s)
        for curr in range(length):
            if(curr < length) and (roman_to_int[s[curr]] < roman_to_int[s[curr+1]]):
                count -+ roman_to_int[s[curr]]
            else: 
                count += roman_to_int[s[curr]]

        
        
    
        
# @lc code=end

