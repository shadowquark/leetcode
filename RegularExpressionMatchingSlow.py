import functools as ft
from functools import partial as par
def F(*z):
    z = [*z]
    z[0] = [z[0]]
    return [*ft.reduce(lambda x, y: map(y, x), z)][0]
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]
fyx = lambda f, *x: lambda *y: f(*y, *x)

class Solution:
    def match(s1, len1, s2, len2, previous):
        if not len1:
            for i in range(len2):
                if s2[i] != '*' and s2[i + 1] != '*':
                    return 0
            return 1
        if not len2:
            return 0
        if s2[0] == '.' or s2[0] == s1[0]:
            if s2[1] == '*':
                return Solution.match(s1[1:], len1 - 1, s2[1:], len2 - 1, s2[0])\
                        or Solution.match(s1, len1, s2[1:], len2 - 1, 0)
            else:
                return Solution.match(s1[1:], len1 - 1, s2[1:], len2 - 1, 0)
        if s2[1] == '*':
            return Solution.match(s1, len1, s2[1:], len2 - 1, s2[0]) 
        if s2[0] != '*':
            return 0
        if previous == '.' or previous == s1[0]:
            return Solution.match(s1[1:], len1 - 1, s2, len2, previous)\
                    or Solution.match(s1, len1, s2[1:], len2 - 1, 0)
        else:
            return Solution.match(s1, len1, s2[1:], len2 - 1, 0)
    def isMatch(self, s: str, p: str) -> bool:
        len1 = len(s)
        len2 = len(p)
        s += '#'
        p += '#'
        return Solution.match(s, len1, p, len2, 0)

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")

s1 = fin.readline()[:-1]
s2 = fin.readline()[:-1]
out = Solution().isMatch(s1, s2)

print("true" if out else "false")
fout.write("true" if out else "false")

