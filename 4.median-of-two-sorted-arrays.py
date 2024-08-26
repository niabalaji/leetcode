#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = set()
# @lc code=end

nums1 = [1,2], nums2 = [3,4]
solution = Solution()
print(solution.findMedianSortedArrays(nums1,nums2))