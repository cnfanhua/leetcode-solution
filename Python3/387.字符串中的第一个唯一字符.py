#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int: 
        if not s:
            return -1
        dic1 = {}

        for i in range(len(s)):
            if s[i] in dic1.keys():
                dic1[s[i]] += 1
            else:
                dic1[s[i]] = 1
        for k, v in dic1.items():
            if v == 1:
                return s.index(k)
        return -1
# @lc code=end

