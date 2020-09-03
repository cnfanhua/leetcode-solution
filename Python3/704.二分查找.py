#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        s = 0
        m = 0
        e = len(nums) - 1
        while s <= e:
            m = (s+e)//2
            if(nums[m] == target):
                return m
            elif target > nums[m]:
                s = m+1
            else:
                e = m-1
        return -1
# @lc code=end
