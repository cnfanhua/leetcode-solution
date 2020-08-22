#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        firstI, nextI = 0, 1

        for i in nums:
            if nums[nextI] == 0:
                nextI = nextI + 1
            elif nums[firstI] != 0:
                firstI = firstI + 1
                if firstI == nextI:
                    nextI = nextI + 1
            else:
                nums[firstI] = nums[nextI]
                nums[nextI] = 0
                firstI = firstI + 1
                nextI = nextI + 1
            if nextI == len(nums):
                break
# @lc code=end
