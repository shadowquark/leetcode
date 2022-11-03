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
    def quicksort(l, r, obj):
        if not l < r:
            return obj
        i, j, x = l, r, obj[r]
        while (i < j):
            while (i < j and obj[i] <= x):
                i += 1
            obj[j] = obj[i]
            while (i < j and obj[j] > x):
                j -= 1
            obj[i] = obj[j]
        obj[i] = x
        Solution.quicksort(l, i - 1, obj)
        Solution.quicksort(i + 1, r, obj)
        return obj
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lenNums = len(nums)
        nums = Solution.quicksort(0, lenNums - 1, nums)
        record, out = {}, []
        for x in nums:
            if x in record:
                record[x] += 1
            else:
                record[x] = 1
        for i in range(lenNums):
            if nums[i] > 0:
                break
            if i and nums[i] == nums[i - 1]:
                continue
            record[nums[i]] -= 1
            for j in range(i + 1, lenNums):
                if nums[i] + nums[j] > 0:
                    break
                if j - i - 1 and nums[j] == nums[j - 1]:
                    continue
                record[nums[j]] -= 1
                test = - nums[i] - nums[j]
                if (test in record and test >= nums[j]
                    and record[test]):
                    out.append([nums[i], nums[j], test])
                record[nums[j]] += 1
            record[nums[i]] += 1
        return out

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")
a = [int(x) for x in fin.readline()[:-1].split(' ')]
out = Solution().threeSum(a)
print(out)
fout.write(str(out))

