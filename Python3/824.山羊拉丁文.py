#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#

# @lc code=start
class Solution:
    def toGoatLatin(self, S: str) -> str:
        if not S:
            return ''

        yy = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

        result = []
        index = 1
        for word in S.split(' '):

            if word[0] in yy:
                tmp = word+'ma'
            else:
                tmp = word[1:] + word[0] + 'ma'
            result.append(tmp+'a'*index)
            index += 1

        return ' '.join(result)
# @lc code=end
