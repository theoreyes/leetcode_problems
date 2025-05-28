# Theodore Reyes
#
# Explanation: Carefully iterates through the first numRows
# letters of the string, and from these letters, performs a
# series of jumps which spell out the zigzag formation of the
# input string. Specifically, the chars are added to a list
# and then joined at the end for sake of efficiency.

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        count = 0
        out = []
        jmpOffset = (numRows - 1) * 2
        if jmpOffset == 0 or numRows >= length: return s
        for i in range(numRows):
            jmpOne = (jmpOffset - i * 2) % jmpOffset
            jmpTwo = jmpOffset - jmpOne
            j = i
            k = 0
            out.append(s[i])
            if jmpOne == 0: # on first or last rows
                while ((j := j + jmpOffset) < length):
                    out.append(s[j])
            else:
                while (j < length):
                    if k % 2 == 0:
                        j += jmpOne
                    else:
                        j += jmpTwo
                    if (j < length): 
                        out.append(s[j])
                        k += 1
        resStr = ''.join(out)
        return resStr
