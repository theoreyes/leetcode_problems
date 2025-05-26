# Theodore Reyes

class Solution:
    def romanToInt(self, s: str) -> int:
        romToInt = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        result = 0
        length = len(s)
        i = 0
        while i < length:
            ch = s[i]
            if (i == (length - 1)):
                result += romToInt[ch]
            else:
                match ch:
                    case 'I':
                        if s[i + 1] == 'V':
                            result += 4
                            i += 1
                        elif s[i + 1] == 'X':
                            result += 9
                            i += 1
                        else:
                            result += romToInt[ch]
                    case 'X':
                        if s[i + 1] == 'L':
                            result += 40
                            i += 1
                        elif s[i + 1] == 'C':
                            result += 90
                            i += 1
                        else:
                            result += romToInt[ch]
                    case 'C':
                        if s[i + 1] == 'D':
                            result += 400
                            i += 1
                        elif s[i + 1] == 'M':
                            result += 900
                            i += 1
                        else:
                            result += romToInt[ch]
                    case _:
                        result += romToInt[ch]
            i += 1
        return result
