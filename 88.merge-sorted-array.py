#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
    # have three pointers : 
        # p1 - counter for nums1 (init to last m)
        # p2 - counter for nums2 (init to last n)
        # p3 - counter for insertion (init at end of nums1)
    # start inserting from the end, to avoid multiple shifts
    # compare nums1[p1] to nums2[p2]
        # if nums1[p1] is larger then nums2[p2]
            # 
        # if nums2[p2] is larger then nums1[p1]: 
            # insert nums[p2] at k position
            # decrement p2 and k
        p1 = m - 1
        p2 = n - 1
        insert = m + n - 1 

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[insert] = nums1[p1]
                p1 = p1 - 1
            else: 
                nums1[insert] = nums2[p2]
                p2 = p2 - 1
            insert = insert - 1
        while p2 >= 0:
            nums1[insert] = nums2[p2]
            p2 = p2 - 1
            insert = insert - 1
                
# @lc code=end

