#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 因多数元素 > 数组的/2
        middleIndex = len(nums)//2
        nums.sort()
        return nums[middleIndex]

        # dict key唯一
        # d = {}
        # for i in nums:
        #     if i in d.keys():
        #         d[i] += 1
        #     else:
        #         d[i] = 1

        # result, count = 0, 0
        # for k, v in d.items():
        #     if v > count:
        #         result = k
        #         count = v
        # if count > len(nums)/2:
        #     return result
        # return -1
# @lc code=end
