# Theodore Reyes
#
# Explanation: Encodes strings by encoding a) the number of strings
# in the input array, and b) for each string in the encoded string,
# includes the number of characters in each string. To decode the
# encoded string, these two pieces of information are parsed by
# decode() and each string appended to an output list to the user.
#
# By encoding both the number of strings as well as each
# string's length (since Python stores this information
# anyways, len() is used here, but is not necessary. If we implemented 
# in a language that did not store this information, we could simply 
# have encode perform this task per string), we are able to efficiently
# slice each string using pointer/index arithmetic on the encoded
# string.

class Solution:

    def encode(self, strs: List[str]) -> str:
        import io
        code = io.StringIO()
        code.write(f"{len(strs)}")
        for s in strs:
            code.write(f"[{len(s)}]") # Encodes length of given str
            code.write(s)             # Encodes the string
        print(code.getvalue())
        return code.getvalue()

    def decode(self, s: str) -> List[str]:
        if (s == '0'): return []      # Edge case: No strings
        output = []
        beg = s.index('[')
        numStrs = int(s[0:beg])
        end = beg
        print(numStrs)
        for i in range(numStrs):
            while (s[end] != "]"): end += 1
            length = int(s[beg + 1: end])
            print(length)
            beg = end + 1
            end = beg + length
            output.append(s[beg : end]) # Decodes string
            print(output)
            beg = end
        return output

