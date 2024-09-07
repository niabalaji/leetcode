#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start

import math
import array
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        
        # Initialize binary search boundaries
        low, high = 0, m
        
        while low <= high:
            # Partition nums1 and nums2
            partitionX = (low + high) // 2
            partitionY = (m + n + 1) // 2 - partitionX
            
            # If there are no elements on the left side of partition, use -inf for maxLeftX
            # Similarly, if there are no elements on the right side of partition, use +inf for minRightX
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]
            # Check if we have found the correct partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # Found the partition
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                # Move towards the left side in nums1
                high = partitionX - 1
            else:
                # Move towards the right side in nums1
                low = partitionX + 1
    
        

# @lc code=end

nums1 = [1,3]
nums2 = [2]
solution = Solution()
print(solution.findMedianSortedArrays(nums1,nums2))