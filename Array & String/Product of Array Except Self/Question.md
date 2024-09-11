# 238. Product of Array Except Self

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

**Example 1:**

Input: `nums = [1,2,3,4]`  
Output: `[24,12,8,6]`  
Explanation:  
- For `answer[0]`, the product of numbers except `1` is `2*3*4 = 24`.  
- For `answer[1]`, the product of numbers except `2` is `1*3*4 = 12`.  
- For `answer[2]`, the product of numbers except `3` is `1*2*4 = 8`.  
- For `answer[3]`, the product of numbers except `4` is `1*2*3 = 6`.

**Example 2:**

Input: `nums = [-1,1,0,-3,3]`  
Output: `[0,0,9,0,0]`  
Explanation:  
- Any product that includes `0` results in `0`.

**Constraints:**

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

**Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array does not count as extra space for space complexity analysis.)
