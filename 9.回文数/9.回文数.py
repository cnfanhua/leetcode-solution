#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            if -2**31 < x < 2**31-1:
                tmp = str(x).replace('-', '')
                tmp = int(tmp[::-1])
                if tmp > 2**31-1:
                    return False

                return x == tmp
            else:
                return False
        else:
            return False
# @lc code=end
