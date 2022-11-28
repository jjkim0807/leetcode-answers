from functools import cache
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for l in range(2, len(nums)+1):
            window = nums[0:l]
            for i in range(1, len(nums)):
                
                pass
