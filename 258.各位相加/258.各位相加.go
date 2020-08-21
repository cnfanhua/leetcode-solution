package adddigits

/*
 * @lc app=leetcode.cn id=258 lang=golang
 *
 * [258] 各位相加
 *	要求的数即为：数字根
 *
 *  原数: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
 *  数根: 1 2 3 4 5 6 7 8 9  1  2  3  4  5  6  7  8  9  1  2  3  4  5  6  7  8  9  1  2  3
 *
 *  即为：num小于10直接返回；num是9的倍数的，9为数字根；其余为num mod 9
 */

// @lc code=start
func addDigits(num int) int {
	if num <= 9 {
		return num
	} else if num%9 == 0 {
		return 9
	}

	return num % 9
}

// @lc code=end
