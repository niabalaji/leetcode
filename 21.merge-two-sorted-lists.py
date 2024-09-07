#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        
        Algorithm Outline:
        Create a dummy node to act as the starting point for the 
        merged list.
        Use two pointers, l1 and l2, to traverse list1 and list2.
        Compare nodes and append the smaller node to the merged list.
        Once one of the lists is exhausted, append the remaining
        nodes of the other list.
        Return dummy.next as the head of the merged list.

        """
        dummyNode = ListNode()
        current = dummyNode

        
         

        
# @lc code=end 
solution = Solution()
list1 = ListNode([1,2,4])
list2 = ListNode([1,3,4])
print(solution.mergeTwoLists(list1,list2))
