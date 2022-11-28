class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""

        # 1000
        i = num // 1000
        result += i * "M"
        num %= 1000

        # 100
        i = num // 100
        if i == 9:
            result += "CM"
        elif i > 4:
            result += "D" + (i-5) * "C"
        elif i == 4:
            result += "CD"
        else:
            result += i * "C"
        num %= 100

        # 10
        i = num // 10
        if i == 9:
            result += "XC"
        elif i > 4:
            result += "L" + (i-5) * "X"
        elif i == 4:
            result += "XL"
        else:
            result += i * "X"
        num %= 10

        # 1
        i = num // 1
        if i == 9:
            result += "IX"
        elif i > 4:
            result += "V" + (i-5) * "I"
        elif i == 4:
            result += "IV"
        else:
            result += i * "I"
        num %= 1

        return result
