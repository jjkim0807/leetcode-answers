from operator import truediv
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 단어 수를 센다
        d = {}
        for w in words:
            if w not in d:
                d[w] = 0
            d[w] += 1
        dl = list(d.items())

        # 단어 수, 알파벳 순서대로 정렬한다
        sdl = sorted(dl, key=lambda x: (-x[1], x[0]))

        # top k개를 리턴한다
        return [x[0] for x in sdl[:k]]
