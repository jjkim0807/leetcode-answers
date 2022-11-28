class StockSpanner:
    def __init__(self):
        self.s = []
        self.j = []

    def next(self, price: int) -> int:
        # s 뒤에서부터 대응하는 j의 값만큼 점프한다
        # 점프한 지점의 값이 price 보다 크거나, 그 지점이 맨 끝이라면
        # 그 지점을 현재 j 값으로 하고, s에 price를 append 한다
        # 점프한 지점의 값이 price 보다 작으면
        # 다시 그 지점에 대응하는 j의 값만큼 점프한다
        # 현재 j 값에서 맨 끝 사이의 길이를 리턴한다.

        cursor = len(self.s) - 1
        while cursor >= 0 and self.s[cursor] <= price:
            cursor = self.j[cursor]
        self.s.append(price)
        self.j.append(cursor)

        return (len(self.s) - 1) - self.j[-1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
