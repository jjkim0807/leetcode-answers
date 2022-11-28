# @before-stub-for-debug-begin
from copy import deepcopy
from python3problem947 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
#

# @lc code=start
from functools import cmp_to_key
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # stones를 바탕으로 graph를 생성함
        # 한 노드를 기점으로 dfs로 탐색하면서 visit된 노드들을 체크함
        # 위 탐색에서 visit된 노드들은 그래프에서 삭제하고, 다시 위 탐색 반복
        # 그래프에 더이상 노드가 남아있지 않으면 현재까지의 depth의 총합을 리턴

        class Graph:
            class Node:
                def __init__(self, x, y) -> None:
                    self.x = x
                    self.y = y
                    self.visited = False
                    self.children = []

                def visit(self):
                    if self.visited:
                        return False
                    else:
                        self.visited = True
                        return True

                def link(self, node):
                    node.children.append(self)
                    self.children.append(node)

            def __init__(self, coords) -> None:
                self.nodes = []
                xmap, ymap = {}, {}
                for x, y in coords:
                    node = self.Node(x, y)
                    self.nodes.append(node)
                    for v, map in [(x, xmap), (y, ymap)]:
                        if v not in map:
                            map[v] = []
                        map[v].append(node)

                for map in [xmap, ymap]:
                    for nodes in map.values():
                        for i in range(0, len(nodes)):
                            for j in range(i+1, len(nodes)):
                                nodes[i].link(nodes[j])

            def clean(self):
                def recursive(node):
                    if node.visit():
                        result = 1
                        for child in node.children:
                            result += recursive(child)
                        return result
                    else:
                        return 0

                assert len(self.nodes) > 0
                result = recursive(self.nodes[0])
                self.nodes = list(filter(lambda x: not x.visited, self.nodes))
                return result

        graph = Graph(stones)
        total = 0
        while len(graph.nodes) > 0:
            result = graph.clean()
            total += result - 1
        return total


# @lc code=end
