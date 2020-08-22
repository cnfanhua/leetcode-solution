#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        minIndex, maxIndex = 0, len(numbers)-1
        while minIndex < maxIndex:
            result = numbers[minIndex] + numbers[maxIndex]
            if result == target:
                return [minIndex+1, maxIndex+1]
            elif result > target:
                maxIndex -= 1
            else:
                minIndex += 1
        return None
        '''minIndex, maxIndex = 0, len(numbers)
        middleIndex = (int((minIndex+maxIndex) / 2))

        while(numbers[middleIndex] > target):
            maxIndex = middleIndex
            middleIndex = (int((minIndex+maxIndex) / 2))

        j = -1
        for i in range(1, len(numbers)):
            temp = numbers[:i]
            if target - numbers[i] in temp:
                j = temp.index(target - numbers[i])
                break

        if j >= 0:
            return [j+1, i+1]

        return None'''
# @lc code=end
