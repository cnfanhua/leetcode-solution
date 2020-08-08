/*
 * @lc app=leetcode.cn id=1 lang=csharp
 *
 * [1] 两数之和
 */

// @lc code=start
public class Solution
{
    public int[] TwoSum(int[] nums, int target)
    {
        var result = new int[2] { -1, -1 };
        for (int i = 0, j = nums.Length; i < j; i++)
        {
            for (int x = i + 1, y = nums.Length - 1; x <= y; x++)
            {
                if (nums[i] + nums[x] == target)
                {
                    result = new int[] { i, x };
                }
            }
        }

        return result;
    }
}
// @lc code=end

