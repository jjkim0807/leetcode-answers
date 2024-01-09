#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#


# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        switch = True
        result = ""
        while len(word1) > 0 and len(word2) > 0:
            if switch:
                result += word1[0]
                word1 = word1[1:]
            else:
                result += word2[0]
                word2 = word2[1:]
            switch = not switch

        while word1:
            result += word1[0]
            word1 = word1[1:]
        while word2:
            result += word2[0]
            word2 = word2[1:]

        return result


# @lc code=end
