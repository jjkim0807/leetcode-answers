from bisect import bisect_left, bisect_right
from collections import namedtuple


class MyCalendarThree:

    class NewStorage:
        Book = namedtuple("Book", ["start", "end"])

        def __init__(self):
            self.borders = [0, 10**9]
            self.heights = [0]
            self.k = 0

        def add(self, b: Book):
            # split `books` with borders of `b`
            self.split(b.start)
            self.split(b.end)

            # split `b` with borders of `books`
            def split_one(b, i):
                raise NotImplementedError

            for i in self.borders: w
                b = split_one(b, i)

            # update `self.k` while merging `b` and `books`
            self.merge(b)

        def split(self, i):
            insert_idx = bisect_left(self.borders, i)
            if self.borders[insert_idx] == i:
                return
            else:
                self.borders.insert(insert_idx, i)

            self.heights.insert(insert_idx, self.heights)

        def check(self):
            return self.k

    def __init__(self):
        self.books = self.NewStorage()

    def book(self, start: int, end: int) -> int:
        self.books.add(self.NewStorage.Book(start, end))
        return self.check()

    def check(self) -> int:
        return self.books.check()


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
