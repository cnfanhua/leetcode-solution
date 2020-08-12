#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        result = ''
        minLength = len(strs[0])
        for item in strs:
            if minLength >= len(item):
                minLength = len(item)

        for i in range(0, minLength):
            instr = True
            firstChar = strs[0][0:i+1]
            for item in strs:
                if item[0:i+1] != firstChar:
                    instr = False
            if instr:
                result = firstChar

        return result

# @lc code=end
