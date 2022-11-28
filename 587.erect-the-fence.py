# @before-stub-for-debug-begin
from python3problem587 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=587 lang=python3
#
# [587] Erect the Fence
#

# @lc code=start
from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        class Line:
            def __init__(self, p1, p2) -> None:
                self.children = [p1, p2]
                self.reversed = False

            def __eq__(self, __o) -> bool:
                for c in __o.children[:2]:
                    if self(c) != 0:
                        return False
                return True

            def __call__(self, coor):
                x, y = coor
                (x1, y1), (x2, y2) = self.children[0], self.children[1]
                result = (y2-y1)*(x-x1)-(x2-x1)*(y-y1)
                return - result if self.reversed else result

            @staticmethod
            def pivot(l1, l2, coor):
                h1, t1 = l1.findEnds()
                h2, t2 = l2.findEnds()
                if h1 == h2:
                    p1 = t1
                    p2 = t2
                elif h1 == t2:
                    p1 = t1
                    p2 = h2
                elif t1 == h2:
                    p1 = h1
                    p2 = t2
                elif t1 == t2:
                    p1 = h1
                    p2 = h2
                else:
                    raise ValueError

                l1 = Line(p1, coor)
                l2 = Line(p2, coor)
                l1.calibrate(p2)
                l2.calibrate(p1)

                return l1, l2

            def split(self, coor):
                h, t = self.findEnds()
                l1, l2 = Line(h, coor), Line(t, coor)
                l1.calibrate(t)
                l2.calibrate(h)
                self.calibrate(coor)

                return l1, l2

            def addChild(self, coor):
                self.children.append(coor)

            def findEnds(self):
                assert len(self.children) > 1
                self.children = sorted(self.children)

                return self.children[0], self.children[-1]

            def calibrate(self, p):
                if self(p) < 0:
                    self.reversed = True

        class Perimeter:
            def __init__(self, line) -> None:
                self.lines = [line]

            def add(self, coor):
                if len(self) == 1:
                    line: Line = self.lines[0]
                    sign = line(coor)
                    if sign == 0:
                        line.addChild(coor)
                    else:
                        l1, l2 = line.split(coor)
                        self.lines.append(l1)
                        self.lines.append(l2)
                elif len(self) > 1:
                    deprecated_lines = []
                    new_lines = []
                    for line in self.lines:
                        sign = line(coor)
                        if sign > 0:
                            new_lines.append(line)
                        elif sign < 0:
                            deprecated_lines.append(line)
                        elif sign == 0:
                            line.addChild(coor)
                            new_lines.append(line)

                    l1, l2 = None, None
                    if deprecated_lines:
                        piviot_lines = []
                        for dl in deprecated_lines:
                            lines = dl.split(coor)
                            for line in lines:
                                if line in piviot_lines:
                                    piviot_lines.remove(line)
                                else:
                                    piviot_lines.append(line)
                        assert (len(piviot_lines) == 2)
                        for line in piviot_lines:
                            if line not in new_lines:
                                new_lines.append(line)
                    self.lines = new_lines
                else:
                    raise ValueError

            def __len__(self):
                return len(self.lines)

            def toPoints(self):
                result = set()
                for line in self.lines:
                    for c in line.children:
                        result.add(tuple(c))
                return result

        def recursive(perimeter: Perimeter, trees: List[Line]):
            """존재하는 테두리에 나무들을 추가하고 났을 때의 테두리를 출력하는 함수"""
            if not perimeter:
                line = Line(trees[0], trees[1])
                perimeter = Perimeter(line)
                return recursive(perimeter, trees[2:])
            elif not trees:
                return perimeter
            else:
                perimeter.add(trees[0])
                return recursive(perimeter, trees[1:])

        if not trees:
            return []
        elif len(trees) == 1:
            return trees
        else:
            perimeter = recursive(None, trees)
            return perimeter.toPoints()


# @lc code=end
