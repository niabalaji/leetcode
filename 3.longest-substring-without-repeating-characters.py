#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charset = set() 
        x = 0
        maxLen = 0

        for y in range(len(s)):
            while s[y] in charset:
                charset.remove[y]
                maxLen+=1
            charset.add[y]
            maxLen= max(maxLen, y-x+1)
            
            

                

        
# @lc code=end

