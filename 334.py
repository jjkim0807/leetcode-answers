from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        class CandidateGroup():
            def __init__(self):
                self.h3 = None
                self.h2 = None
                self.h1 = None

            def add(self, num):
                # h2에 num을 넣으면 h3로 넘어갈 수 있는 것들이 있으면 넘기기
                if self.h2:
                    if self.h2[-1] < num:
                        self.h3 = self.h2 + [num]
                        return

                # h2에서 h3로 넘어간 것들이 없으면 h1에서 h2 넘어갈 수 있는 것들이 있으면 넘기기
                if self.h1:
                    if self.h1[-1] < num:
                        self.h2 = self.h1 + [num]
                        return

                # h1에서 h2로 넘어간 것들이 없으면 num이 h1의 요소보다 작으면 교체하기
                if not self.h1:
                    self.h1 = [num]
                    return
                else:
                    if self.h1[-1] > num:
                        self.h1 = [num]
                        return

            def detect(self):
                # h3가 채워져 있는지 확인
                return self.h3 != None

        cg = CandidateGroup()
        for num in nums:
            cg.add(num)
            if cg.detect():
                return True
        return False
