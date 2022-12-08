from typing import List
from functools import partial as par
import functools as ft
import sys
import bisect
def F(*z):
    z = [*z]
    z[0] = [z[0]]
    return [*ft.reduce(lambda x, y: map(y, x), z)][0]
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]
fyx = lambda f, *x: lambda *y: f(*y, *x)

class Solution:
    def quicksort(l, r, obj, rank):
        if (l >= r):
            return
        i, j, x = l, r, obj[r]
        while (i < j):
            while i < j and obj[i][rank] <= x[rank]:
                i += 1
            obj[j] = obj[i]
            while i < j and obj[j][rank] > x[rank]:
                j -= 1
            obj[i] = obj[j]
        obj[i] = x
        Solution.quicksort(l, i - 1, obj, rank)
        Solution.quicksort(i + 1, r, obj, rank)
    def findpos(x, y):
        n = len(x) - 1
        if (y >= x[-1]):
            return n
        l, r = 0, n - 1
        while 1:
            if y < x[(l + r) // 2]:
                r = (l + r) // 2 
            else:
                l = (l + r) // 2 + 1
            if (y < x[l]):
                return l - 1
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        n = len(startTime)
        obj = [*zip(startTime, endTime, profit)]
        obj.sort(key = lambda x: x[1])
#       sys.setrecursionlimit(50001)
#       Solution.quicksort(0, n - 1, obj, 1)
        out = [[0], [0]]
        for s, e, p in obj:
#           pos = Solution.findpos(out[1], s)
            pos = bisect.bisect(out[1], s) - 1
            if (out[0][pos] + p > out[0][-1]):
                out[0].append(out[0][pos] + p)
                out[1].append(e)
        return out[0][-1]

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")

n = int(fin.readline())
startTime = [int(x) for x in fin.readline().split(',')]
endTime = [int(x) for x in fin.readline().split(',')]
profit = [int(x) for x in fin.readline().split(',')]

out = Solution().jobScheduling(startTime, endTime, profit)
print(out)
F(out, str, fout.write)

