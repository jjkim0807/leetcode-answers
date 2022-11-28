from bisect import bisect_right
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        class Storage:
            def __init__(self) -> None:
                self.pairs = []

            def __contains__(self, x):
                # pairs는 오름차순으로 정렬되어 있다.
                # bisect를 이용해 x가 들어있을만한 pair를 찾는다.
                idx = bisect_right(self.pairs, x, key=lambda e: e[0]) - 1

                # 해당 pair에 x가 들어있는지 확인한다.
                if 0 <= idx and idx < len(self.pairs):
                    s, e = self.pairs[idx]
                    if s <= x and x <= e:
                        return True
                return False

            def add(self, x):
                # pairs는 오름차순으로 정렬되어야 한다.
                # bisect를 이용해 x가 들어가야 할 자리를 찾는다.
                idx = bisect_right(self.pairs, x, key=lambda e: e[0])

                # 해당 자리에 x를 추가한다.
                self.pairs.insert(idx, [x, x])

                # 추가된 pair와 합칠 수 있는 pair가 좌우에 있으면 합친다.
                self.merge(idx)
                self.merge(idx-1)

            def merge(self, idx):
                if 0 <= idx and idx < len(self.pairs)-1:
                    if self.pairs[idx][1]+1 == self.pairs[idx+1][0]:
                        self.pairs[idx][1] = self.pairs[idx+1][1]
                        del self.pairs[idx+1]

            def findMissingNum(self):
                # 연속된 수 중에서 한 문자만 빠져있다.
                # pairs의 개수가 1이라면 양 끝 중 하나일 것이다.
                if len(self.pairs) == 1:
                    if self.pairs[0][0] == 1:
                        return self.pairs[0][1] + 1
                    else:
                        return 1

                # pairs의 개수가 2라면 그 중간 숫자일 것이다.
                elif len(self.pairs) == 2:
                    return self.pairs[0][1] + 1

                else:
                    raise ValueError

        # 범위를 나타내는 pair들을 가지고 현재까지 발견된 숫자들을 저장하자.
        s = Storage()

        # 저장하는 중에 중복되는 입력이 들어온 경우 기억해둔다.
        d = None
        for n in nums:
            if n in s:
                d = n
            else:
                s.add(n)

        # 저장이 완료되면 빠진 숫자가 무엇인지 알아낸다.
        m = s.findMissingNum()

        # 정답을 출력한다.
        return [d, m]
