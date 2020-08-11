#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        specRoman = {'IV': 4, 'IX': 9, 'XL': 40,
                     'XC': 90, 'CD': 400, 'CM': 900}
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}

        inputS = s
        for k, v in specRoman.items():
            inputS = inputS.replace(k, str(v)+',')

        for k, v in roman.items():
            inputS = inputS.replace(k, str(v)+',')

        result = 0

        for item in inputS.split(','):
            if item == '':
                continue
            result = result + int(item)

        if 1 <= result <= 3999:
            return result
        else:
            return 0

# @lc code=end
