#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        c = nums.count(0)
        while True:
            if i >= len(nums) - c:
                break
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i += 1

        return nums


# @lc code=end
