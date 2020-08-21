#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # set() 函数创建一个无序不重复元素集
        num_set = set(nums)

        num_set_len = len(num_set)+1
        for i in range(0, num_set_len):
            if i not in num_set:
                return i
        return -1

        # 比下面快一点，， 76ms
        '''dic = {}
        for i in nums:
            dic[i] = i

        numsLen = len(nums)+1
        for i in range(0, numsLen+1):
            if i not in dic.keys():
                return i
        return -1'''

        # 太慢... 1000ms+
        '''if not nums:
            return -1
        nums.sort()
        numsLen = len(nums)

        for i in range(0, numsLen+1):
            if i not in nums:
                return i
        return -1'''
# @lc code=end
