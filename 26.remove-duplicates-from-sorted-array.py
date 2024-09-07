#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nset = set()
        while(len(nums) != 0):
            for x in nums: 
                if x not in nset:
                    nset.add(x)
        return len(nums)        
        
# @lc code=end
solution = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(solution.removeDuplicates(nums))