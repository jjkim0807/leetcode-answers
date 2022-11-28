class Solution:
    def makeGood(self, s: str) -> str:
        def makeBetter(s):
            for i in range(1, len(s)):
                if s[i-1] != s[i] and s[i-1].lower() == s[i].lower():
                    return makeBetter(s[:i-1] + s[i+1:])
            return s
        return makeBetter(s)
