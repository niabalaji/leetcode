#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # iterate through the array of strings and 
        # check the first 
        if not strs: 
            return ""
        
        prefix = strs[0]
        
        for string in strs:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix: 
                    return ""
        return prefix

        
# @lc code=end

