#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:

    def __init__(self, nums: [int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        numsLen = len(self.nums)
        if j > numsLen-1:
            j = numsLen - 1
        result = 0
        for i in range(i, j+1):
            result += self.nums[i]
        return result

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end
