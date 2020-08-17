#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 最优解，按位或
        # return reduce(lambda x, y: x ^ y, nums)

        for n in nums:
            if nums.count(n) == 1:
                return n
        return None
# @lc code=end
