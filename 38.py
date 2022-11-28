class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n > 1:
            result = ""
            prev = None
            count = 0
            for cur in self.countAndSay(n-1):
                if prev == cur:
                    count += 1
                else:
                    if prev != None:
                        result += str(count)
                        result += prev
                    count = 1
                    prev = cur
            result += str(count)
            result += prev

            return result
        else:
            raise ValueError
