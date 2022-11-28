from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def strToBitmap(s):
            result = 0
            for c in s:
                cur = 1 << (ord(c) - ord('a'))
                if result & cur > 0:
                    return 0
                result |= cur
            return result

        def countBitmap(bitmap):
            count = 0
            while bitmap > 0:
                if (bitmap & 1) == 1:
                    count += 1
                bitmap >>= 1
            return count

        # 모든 문자열들의 사용된 알파벳을 나타내는 비트맵과 unique character 개수를 구한다
        # 이때 해당 문자열 자체에 중복된 알파벳이 있는 경우 0으로 표기한다
        bitmaps = []
        for s in arr:
            bitmaps.append(strToBitmap(s))

        # 재귀적으로
        # 입력된 비트맵을 바탕으로 가장 긴 길이를 리턴한다
        def rec_maxLength(bg_b, in_bitmaps):
            max_length = countBitmap(bg_b)
            for i, b in enumerate(in_bitmaps):
                if (bg_b & b > 0) or (b == 0):
                    continue
                else:
                    rec_result = rec_maxLength(bg_b | b, in_bitmaps[i+1:])
                    if rec_result > max_length:
                        max_length = rec_result
            return max_length

        return rec_maxLength(0, bitmaps)
