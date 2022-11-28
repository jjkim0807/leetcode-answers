#
# @lc app=leetcode id=1893 lang=python3
#
# [1893] Check if All the Integers in a Range Are Covered
#

# @lc code=start


from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        bitmap = [False] * (right-left+1)
        for s, e in ranges:
            for i in range(s-left, e-left+1):
                if 0 <= i and i < len(bitmap):
                    bitmap[i] = True
        return all(bitmap)


# @lc code=end
