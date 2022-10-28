import functools as ft
from functools import partial as par
from typing import List
def F(*z):
    z = [*z]
    return [*ft.reduce(lambda x, y: map(y, x), [z[:1]] + z[1:])][0]     
FF = lambda *z: [*ft.reduce(lambda x, y: map(y, x), z)]
fyx = lambda f, *x: lambda *y: f(*y, *x)

class Solution:
    def findPos(a, length, num):
        if a[0] > num:
            return 0
        begin, end, pos = 0, length, length // 2
        while 1:
            if a[pos] <= num and (pos == length - 1 or a[pos + 1] > num):
                return pos + 1
            if a[pos] > num:
                pos, end = (begin + pos) // 2, pos
            else:
                begin, pos = pos, (pos + end) // 2
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        flag, len1, len2 = 0, len(nums1), len(nums2)
        medianPos = (len1 + len2) // 2 + 1
        if not (len1 + len2) & 1:
            flag = 1
            medianPos -= 1
        if not len1:
            return (nums2[medianPos - 1] + nums2[medianPos + flag - 1]) / 2
        if not len2:
            return (nums1[medianPos - 1] + nums1[medianPos + flag - 1]) / 2
        begin1 = begin2 = 0
        while 1:
            smaller = Solution.findPos(nums1[begin1:], len1, nums2[begin2])
            if medianPos <= smaller:
                if not flag: 
                    return nums1[begin1 + medianPos - 1] 
                if medianPos - smaller:
                    return (nums1[begin1 + medianPos - 1]
                            + nums1[begin1 + medianPos]) / 2
                return (nums1[begin1 + smaller - 1] + nums2[begin2]) / 2
            len1 -= smaller
            medianPos -= smaller
            if not len1:
                return (nums2[begin2 + medianPos - 1]
                        + nums2[begin2 + medianPos - 1 + flag]) / 2 
            begin1 += smaller
            smaller = Solution.findPos(nums2[begin2:], len2, nums1[begin1])
            if medianPos <= smaller:
                if not flag:
                    return nums2[begin2 + medianPos - 1]
                if medianPos - smaller:
                    return (nums2[begin2 + medianPos - 1]
                            + nums2[begin2 + medianPos]) / 2
                return (nums2[begin2 + smaller - 1] + nums1[begin1]) / 2
            len2 -= smaller
            medianPos -= smaller
            if not len2:
                return (nums1[begin1 + medianPos - 1]
                        + nums1[begin1 + medianPos - 1 + flag]) / 2
            begin2 += smaller

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")

nums1 = [int(x) - int('0') for x in fin.readline()[:-1].split(' ')]
nums2 = [int(x) - int('0') for x in fin.readline()[:-1].split(' ')]
print(Solution().findMedianSortedArrays(nums1, nums2))
F(Solution().findMedianSortedArrays(nums1, nums2), str, fout.write)

