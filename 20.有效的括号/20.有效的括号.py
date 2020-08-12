#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        sLen = len(s)

        if len(s) % 2 != 0:
            return False
        kv = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i in range(0, sLen):
            if s[i] in '{' or s[i] in '[' or s[i] in '(':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                else:
                    if kv[stack[len(stack)-1]] == s[i]:
                        stack.pop()

        return len(stack) == 0
# @lc code=end
