#
# @lc app=leetcode id=1896 lang=python3
#
# [1896] Minimum Cost to Change the Final Value of Expression
#

# @lc code=start
from typing import List, Optional


class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        class Node:
            val = None

        class BrNode(Node):
            def __init__(self, child) -> None:
                super().__init__()
                self.child = child
                self.val = child.val

        class OpNode(Node):
            left = None
            op = None
            right = None

            def __init__(self, left: Node, op: str, right: Node) -> None:
                super().__init__()
                self.left = left
                self.op = op
                self.right = right

                if self.op == "|":
                    self.val = self.left.val | self.right.val
                elif self.op == "&":
                    self.val = self.left.val & self.right.val
                else:
                    raise ValueError

        class ValNode(Node):
            def __init__(self, val: str) -> None:
                super().__init__()
                self.val = int(val)

        def create_node(exp: str):
            stack = []
            for i, c in enumerate(exp):
                if c.isnumeric():
                    if (not stack) or (stack[-1] is "("):
                        stack.append(ValNode(c))
                    elif stack[-1] in {"&", "|"}:
                        while (stack) and (stack[-1] in {"&", "|"}):
                            right = ValNode(c)
                            op = stack.pop()
                            left = stack.pop()
                            stack.append(OpNode(left, op, right))
                elif c in {"&", "|"}:
                    stack.append(c)
                elif c is "(":
                    stack.append(c)
                elif c is ")":
                    merged = stack.pop()
                    stack.pop()
                    while (stack) and (stack[-1] in {"&", "|"}):
                        right = merged
                        op = stack.pop()
                        left = stack.pop()
                        merged = OpNode(left, op, right)
                    stack.append(merged)
                else:
                    raise ValueError

            root = stack.pop()
            return root

        def rec_minOperationsToFlip(node):
            # 해당 노드가 val 노드면
            if isinstance(node, ValNode):
                return 1
            # 해당 노드가 op 노드면
            elif isinstance(node, OpNode):
                # 연산자를 바꾸는 것만으로 전환이 되면 (1&0 or 1|0 or 0&1 or 0|1)
                if node.left.val != node.right.val:
                    return 1

                # 아니면 각 노드의 원래 값을 가지고 주먹구구로 최소 결과를 찾아 리턴한다.
                else:
                    left = rec_minOperationsToFlip(node.left)
                    right = rec_minOperationsToFlip(node.right)

                    # 0&0 or 1|1
                    if (node.left.val == 0 and node.op == "&") or (
                        node.left.val == 1 and node.op == "|"
                    ):
                        # 왼쪽 오른쪽 하나를 바꾸고 연산자까지 바꾸면 됨
                        return 1 + min(left, right)
                    # 0|0 or 1&1
                    elif (node.left.val == 0 and node.op == "|") or (
                        node.left.val == 1 and node.op == "&"
                    ):
                        # 왼쪽 오른쪽 하나를 바꾸기만 하면 됨
                        return min(left, right)
            else:
                raise ValueError

        # expression을 class Node로 변환한다
        node = create_node(expression)

        # 재귀함수 rec_minOperationsToFlip 에 루트노드를 넣고 결과값을 찾도록 한다.
        return rec_minOperationsToFlip(node)


# @lc code=end
