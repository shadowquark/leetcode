class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        m, n = dividend, divisor
        if (m > 0 and n > 0
            or m < 0 and n < 0):
            sign = 1
        else:
            sign = -1
        if n == -1 << 31:
            if m == -1 << 31:
                return 1
            else:
                return 0
        if n < 0:
            n = -n
        flag = 0
        if m < 0:
            if m == -1 << 31:
                m = 2147483647
                flag = 1 if sign < 0 else 0
            else:
                m = -m
        bigFlag = n >> 30
        if bigFlag:
            return int(m >= n) if sign > 0 else - int(m >= n)
        s = 0
        while m >= n:
            base, temp = 1, n
            while m >= temp << 1:
                temp <<= 1
                base <<= 1
            s += base
            m -= temp
            if flag:
                m += 1
                flag = 0
        if sign > 0:
            return s
        else:
            return -s

fin = open("oo.xx", "r")
m, n = [int(x) for x in fin.readline().split(' ')]
out = Solution().divide(m, n)
print(out)

