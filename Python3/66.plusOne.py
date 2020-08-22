#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp = False
        r_digits = digits[::-1]
        for i in range(0, len(r_digits)):
            if r_digits[i]+1 >= 10:
                r_digits[i] = 0
                tmp = True
            else:
                r_digits[i] = r_digits[i]+1
                tmp = False
                break
        if tmp:
            r_digits.append(1)
        return r_digits[::-1]
# @lc code=end
