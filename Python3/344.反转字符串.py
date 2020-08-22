#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return

        first, last = 0, len(s)-1

        while first < last:
            tmp = s[first]
            s[first] = s[last]
            s[last] = tmp
            first += 1
            last -= 1

# @lc code=end
