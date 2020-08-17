#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        # isalnum() 检测字符串是否由字母和数字组成
        # 只考虑数字和字符不考虑标点符号
        # lower()  返回将所有大写字符转换为小写后生城的字符串
        s = ''.join(c for c in s if c.isalnum()).lower()

        return s == s[::-1]
# @lc code=end
