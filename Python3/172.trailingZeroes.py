#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 0的个数取决于n中2和5的个数
        # 而 2 的个数是远远多余 5 的个数的, 因此求出 5 的个数即可

        result = 0
        while n/5 != 0:
            n = n//5
            result += n
        return result

        # Time Limit Exxceeded
        '''if n < 0:
            return 0

        result = 1
        for i in range(1, n+1):
            result *= i
        r_result = str(result)[::-1]
        count0 = 0
        for r in r_result:
            if r != '0':
                break
            count0 += 1
        return count0'''

# @lc code=end
