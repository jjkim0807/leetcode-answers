#
# @lc app=leetcode id=1598 lang=python3
#
# [1598] Crawler Log Folder
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        counter = 0
        for log in logs:
            # if log is "../"" and counter is over 0, then counter -= 1
            if log == "../":
                if counter > 0:
                    counter -= 1
                else:
                    continue

            # elif log is "./", then do nothing
            elif log == "./":
                continue

            # else counter += 1
            else:
                counter += 1

        return counter


# @lc code=end
