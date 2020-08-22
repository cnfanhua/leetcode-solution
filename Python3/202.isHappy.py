#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        dic = {}
        while True:
            if n == 1:
                return True
            elif n > sys.maxsize:
                return False

            if n not in dic.keys():
                dic[n] = 1
            else:
                dic[n] += 1

            if dic[n] > 1:
                return False

            tmp = 0
            for i in str(n):
                tmp += int(i)**2
            n = tmp
# @lc code=end
