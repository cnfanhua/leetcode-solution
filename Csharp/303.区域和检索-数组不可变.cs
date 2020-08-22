/*
 * @lc app=leetcode.cn id=303 lang=csharp
 *
 * [303] 区域和检索 - 数组不可变
 */

// @lc code=start
public class NumArray
{
    public List<int> nums_sum = new List<int>() { 0 };

    public NumArray(int[] nums)
    {
        for (var i = 0; i < nums.Length; i++)
        {
            nums_sum.Add(nums_sum[i] + nums[i]);
        }
    }

    public int SumRange(int i, int j)
    {
        return nums_sum[j + 1] - nums_sum[i];
    }

}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.SumRange(i,j);
 */
// @lc code=end

