#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        while head.next:
            x +=1
            return x
# @lc code=end

solution = Solution()
head = ListNode([1,2,3,4,5])
n = 2
print(solution.removeNthFromEnd(head,n))