from typing import List
import functools as ft
from functools import partial as par
def F(*z):
    z = [*z]
    z[0] = [z[0]]
    return [*ft.reduce(lambda x, y: map(y, x), z)][0]
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]
fyx = lambda f, *x: lambda *y: f(*y, *x)

class Solution:
    def generate(self, ss, s, l, r):
        if (l == r):
            if (s):
                ss.append(s)
            return ss
        for x in self.phone[int(self.digits[l]) - int('2')]:
            s += x
            ss = self.generate(ss, s, l + 1, r)
            s = s[:-1]
        return ss
    def letterCombinations(self, digits: str) -> List[str]:
        self.digits, out = digits, []
        self.phone = ["abc", "def", "ghi", "jkl",
                        "mno", "pqrs", "tuv", "wxyz"]
        out = self.generate([], '', 0, len(digits))
        return out

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")
a = fin.readline()[:-1]
out = Solution().letterCombinations(a)
for x in out:
    print(x)
    fout.write(x)

