import functools as ft
from functools import partial as par
def F(*z):
    z = [*z]
    return [*ft.reduce(lambda x, y: map(y, x), [z[:1]] + z[1:])][0]
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]
fyx = lambda f, *x: lambda *y: f(*y, *x)
class Solution:
    def reverse(self, x: int) -> int:
        if x == -2147483648:
            return 0
        flag = 1 if x < 0 else 0
        x = -x if flag else x
        headFlag, s = 0, []
        upperLimit = [2, 1, 4, 7, 4, 8, 3, 6, 4, 7] 
        while x:
            if x % 10:
                s.append(x % 10)
                headFlag = 1
            elif headFlag:
                s.append(x % 10)
            x //= 10
        lens = len(s)
        if not len(s):
            return 0
        if lens == 10:
            for i in range(10):
                if s[i] > upperLimit[i]:
                    return 0
                if s[i] < upperLimit[i]:
                    break
        out, base = 0, 1
        s = s[::-1]
        for x in s[:-1]:
            out += x * base
            base *= 10
        out += s[-1] * base
        return -out if flag else out
        
fin = open("oo.xx", "r")
fout = open("xx.oo", "w")
n = int(fin.readline())
out = Solution().reverse(n)
print(out)
F(out, str, fout.write)

