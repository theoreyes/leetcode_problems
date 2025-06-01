# Theodore Reyes
#
# Explanation: Finds the largest string that divides both str1 and str2 by
# calculating their intersecting common factors and checking if substrings
# of these lengths (starting from the largest) successfully divide both
# strings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        length1 = len(str1)
        length2 = len(str2)
        pFactors1 = [1, length1]
        pFactors2 = [1, length2]
        cFactors = [1]
        i = 2
        halfLen1 = length1 // 2 if length1 > 3 else length1
        while i <= halfLen1:
            if (length1 % i == 0) : pFactors1.append(i)
            i += 1
        i = 2
        halfLen2 = length2 // 2 if length2 > 3 else length2
        while i <= halfLen2:
            if (length2 % i == 0): 
                pFactors2.append(i)
                if i in pFactors1 : cFactors.append(i)
            i += 1
        if length2 % length1 == 0 and length1 != 1 : cFactors.append(length1)
        if length1 % length2 == 0 and length2 != 1 : cFactors.append(length2)
        for factor in reversed(cFactors):
            divStr = str1[0:factor]
            if (self.stringDivide(divStr, str1, length1, factor) and 
               self.stringDivide(divStr, str2, length2, factor)):
               return divStr
        return ""
            
    def stringDivide(self, divStr, origStr, length, factor):
        for i in range(0, length, factor):
            if origStr[i:i + factor] != divStr : return False
        return True
