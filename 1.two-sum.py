#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nummap = {} 
        other = 0 
        for i,num in enumerate(nums):
            other = target - num 
            if other in nummap:
                return [nummap[other],i] # nummap[other] returns value = index
            nummap[num] = i 
            

# Example usage
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))