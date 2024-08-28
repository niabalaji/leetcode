#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        1. Initialize an empty stack.
        2. For each character in the string:
            a. If it is an opening bracket, push it onto the stack.
            b. If it is a closing bracket:
                i. If the stack is empty, return false (no matching opening bracket).
                ii. If the stack is not empty, check the top of the stack:
                    - If the top is `matching_brackets[closing_bracket]`, pop the top of the stack.
                    - Otherwise, return false.
        3. After the loop, if the stack is empty, return true (all brackets matched).
        4. If the stack is not empty, return false (some unmatched opening brackets).
        """
        bracket = {'(': ')', '{':'}', '[':']'}

        stack = [] 
        
        for char in s: 
            if char in bracket:
                stack.append(char)
            elif char == bracket.values:
                if (len(stack) == 0):
                    return False
                else: 
                    if(bracket[stack[-1]]==char):
                        stack.pop()
                    else: 
                        return False
                    
        return (len(stack) == 0)



            
                

# @lc code=end

