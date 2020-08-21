#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) != 1:
            tmp = 0
            for n in str(num):
                tmp += int(n)
            num = tmp
        return num
# @lc code=end
