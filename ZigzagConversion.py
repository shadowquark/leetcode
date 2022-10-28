import functools as ft
from functools import partial as par
def F(*z):
    z = [*z]
    return [*ft.reduce(lambda x, y: map(y, x), [z[:1]] + z[1:])][0]
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]
fyx = lambda f, *x: lambda *y: f(*y, *x)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        a = [[] for _ in range(numRows)]
        m, length = 2 * numRows - 2, len(s)
        for i in range(length):
            test = i % m if m else 0
            if test < numRows:
                a[test].append(s[i])
            else:
                a[m - test].append(s[i])
        out = ''
        for x in a:
            out += ''.join(x)
        return out

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")
s = fin.readline()[:-1]
n = int(fin.readline())
run = Solution()
print(run.convert(s, n))
fout.write(run.convert(s, n))

