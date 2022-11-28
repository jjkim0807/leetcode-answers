from bisect import bisect_left
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        class Storage:
            def __init__(self) -> None:
                self.s = []

            def add(self, e):
                i = bisect_left(self.s, e)
                self.s.insert(i, e)

            def remove(self, e):
                i = bisect_left(self.s, e)
                if i != len(self.s) and self.s[i] == e:
                    self.s = self.s[:i] + self.s[i+1:]
                else:
                    raise ValueError

            def __contains__(self, e):
                i = bisect_left(self.s, e)
                if i != len(self.s) and self.s[i] == e:
                    return True
                else:
                    return False

        window = Storage()
        for i in range(k):
            if i >= len(nums):
                return False
            if nums[i] not in window:
                window.add(nums[i])
            else:
                return True

        for i in range(k, len(nums)):
            if nums[i] not in window:
                window.add(nums[i])
            else:
                return True
            window.remove(nums[i-k])

        return False
