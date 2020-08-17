#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for n2Data in nums2:
            try:
                nums1[m] = n2Data
                m = m+1
            except:
                nums1.append(n2Data)

        nums1.sort()
# @lc code=end
