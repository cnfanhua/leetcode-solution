/*
 * @lc app=leetcode.cn id=26 lang=csharp
 *
 * [26] 删除排序数组中的重复项
 */

// @lc code=start
public class Solution
{
    public int RemoveDuplicates(int[] nums)
    {
        int numsLength = nums.Length;
        if (numsLength == 0)
        {
            return 0;
        }

        int i = 0;

        for (int j = 1; j < numsLength; j++)
        {
            if (nums[i] != nums[j])
            {
                i++;
                nums[i] = nums[j];
            }
        }

        return i + 1;
    }
}
// @lc code=end

