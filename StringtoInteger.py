import functools as ft
from functools import partial as par
def F(*z):
    z = [*z]
    z[0] = [z[0]]
    return [*ft.reduce(lambda x, y: map(y, x), z)][0]
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]
fyx = lambda f, *x: lambda *y: f(*y, *x)

class Solution:
    def myAtoi(self, s: str) -> int:
        s += '#'
        flag = begin = 0
        while s[begin] == ' ':
            begin += 1
        if s[begin] == '-' or s[begin] == '+':
            flag = 1 if s[begin] == '-' else 0
            begin += 1
        if ord(s[begin]) - ord('0') < 0 or ord(s[begin]) - ord('0') > 9:
            return 0
        while s[begin] == '0':
            begin += 1
        end = begin
        while ord(s[end]) - ord('0') >= 0 and ord(s[end]) - ord('0') <= 9:
            end += 1
        if begin == end:
            return 0
        check = end - begin
        if check > 10:
            return -2147483648 if flag else 2147483647
        a = [2, 1, 4, 7, 4, 8, 3, 6, 4, 8]\
                if flag else [2, 1, 4, 7, 4, 8, 3, 6, 4, 7]
        if check == 10:
            loop = 1
            for i in range(begin, end):
                if int(s[i]) > a[i - begin]:
                    return -2147483648 if flag else 2147483647
                if int(s[i]) < a[i - begin]:
                    loop = 0
                    break
            if loop:
                return -2147483648 if flag else 2147483647
        out = int(s[begin:end])
        return -out if flag else out


fin = open("oo.xx", "r")
fout = open("xx.oo", "w")
s = fin.readline()
out = Solution().myAtoi(s)
print(out)
F(out, str, fout.write)

