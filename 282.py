from functools import cache
from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        def addOperatorsNoPlusMinus(num):
            

        def addOperatorsNoPlus(num):
            raise NotImplementedError

        @cache
        def dpAddOperators(num, target):
            if len(num) == 1 and int(num) == target:
                return [num]

            results = []
            for i in range(1, len(num)):
                heads = addOperatorsNoPlus(num[:i])
                for head in heads:
                    tails = dpAddOperators(num[i:], target - eval(head))
                    results += list(map(lambda x: head + "+" + x, tails))
            return results

        return dpAddOperators(num, target)
