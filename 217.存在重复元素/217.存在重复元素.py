#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        dic = {}
        for n in nums:
            if n in dic.keys():
                dic[n] += 1
            else:
                dic[n] = 1

            if dic[n] >= 2:
                return True

        return False
# @lc code=end
