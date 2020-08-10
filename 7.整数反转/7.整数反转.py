#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if -2**31 < x < 2**31-1:
            tmp = str(x).replace('-', '')
            tmp = int(tmp[::-1])
            if tmp > 2**31-1:
                return 0

            if x > 0:
                return tmp
            else:
                return -tmp

        else:
            return 0
# @lc code=end
