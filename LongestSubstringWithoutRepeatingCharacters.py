import functools as ft
from functools import partial as par
def F(*z):
    z = [*z]
    return [*ft.reduce(lambda x, y: map(y, x), [z[:1]] + z[1:])][0]
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]
fyx = lambda f, *x: lambda *y: f(*y, *x)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = maxlength = 0
        check = []
        for x in s:
            if x in check:
                if length > maxlength:
                    maxlength = length
                pos = check.index(x)
                length -= pos
                temp = check[:pos + 1]
                check = check[pos + 1:]
                del(temp)
                check.append(x)
            else:
                check.append(x)
                length += 1
        if (length > maxlength):
            maxlength = length
        return maxlength

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")

s = fin.readline()[:-1]
F(s, Solution().lengthOfLongestSubstring, str, fout.write)

