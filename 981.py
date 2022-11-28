from bisect import bisect, bisect_right, insort
from collections import namedtuple
from operator import attrgetter

class TimeMap:
    TimeMapElement = namedtuple('TimeMapElement', ('value', 'timestamp'))
    TimeMapElementKey = attrgetter('timestamp')

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        insort(self.storage[key], self.TimeMapElement(value, timestamp), key=self.TimeMapElementKey)

    def get(self, key: str, timestamp: int) -> str:
        def find_le(a, x, key):
            'Find rightmost value less than or equal to x'
            i = bisect_right(a, x, key=key)
            if i:
                return a[i-1]
            else:
                raise ValueError
        try: 
            result = find_le(self.storage[key], timestamp, self.TimeMapElementKey)
            return result.value
        except:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)