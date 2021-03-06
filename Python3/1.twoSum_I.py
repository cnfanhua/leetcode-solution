#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsLens = len(nums)
        j = -1
        for i in range(1, numsLens):
            temp = nums[:i]
            if target - nums[i] in temp:
                j = temp.index(target - nums[i])
                break

        if j >= 0:
            return [j, i]

        return None

# @lc code=end
