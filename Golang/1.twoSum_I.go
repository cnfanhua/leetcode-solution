package twosum

/*
 * @lc app=leetcode.cn id=1 lang=golang
 *
 * [1] 两数之和
 */

// @lc code=start

func twoSum(nums []int, target int) []int {

	var result []int

	numsLength := len(nums)

	for i := 0; i < numsLength; i++ {
		for j := i + 1; j < numsLength; j++ {
			if nums[i]+nums[j] == target {
				result[0] = i
				result[1] = j

				return result
			}
		}
	}

	return nil
}

// @lc code=end
