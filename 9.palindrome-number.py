#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        left = ""
        right = ""
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        original_x = x

        # Reverse half of the number
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Check for palindrome: reversed_half should match x or        reversed_half without the middle digit
        return x == reversed_half or x == reversed_half // 10
        
# @lc code=end
solution = Solution()
x = 101
print(solution.isPalindrome(x))