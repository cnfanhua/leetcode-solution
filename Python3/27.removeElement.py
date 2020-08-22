#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    # version 1
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     dic = {}
    #     index = 0
    #     for i in nums:
    #         if i == val:
    #             continue
    #         dic[index] = i
    #         index = index+1
    #     p = 0
    #     for k in dic:
    #         nums[p] = dic[k]
    #         p = p+1

    #     return len(dic)
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)

        return len(nums)
# @lc code=end
