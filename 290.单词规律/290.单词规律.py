#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if not pattern or not str:
            return False
        str0 = str.strip().split(' ')

        if len(pattern) != len(str0):
            return False
        dic = {}
        dic[pattern[0]] = str0[0]

        for i in range(1, len(pattern)):
            print(dic)
            if pattern[i] in dic.keys():
                if dic[pattern[i]] != str0[i]:
                    return False
            else:
                tmpK = None
                try:
                    tmpK = list(dic.keys())[list(dic.values()).index(str0[i])]
                except:
                    tmpK = None

                if tmpK and tmpK != str0[i]:
                    return False
                dic[pattern[i]] = str0[i]

        return True

        '''
        str0 = str.split(' ')

        if len(str0) != len(pattern):
            return False

        # set(): 将创建一个不重复的元素集
        # zip(): 将对象中对应的元素打包成一个元祖，然后返回这些元祖组成的列表
        if len(set(pattern)) == len(set(str0)) == len(set(zip(list(pattern), str0))):
            return True
        else:
            return False
        '''


# @lc code=end
