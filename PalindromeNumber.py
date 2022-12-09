class Solution:
    def isPalindrome(self, x: int) -> bool:
        out = []
        if x < 0:
            return 0
        while x > 0:
            out.append(x % 10)
            x //= 10
        if out == out[::-1]:
            return 1
        else:
            return 0

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")
n = int(fin.readline())
out = Solution().isPalindrome(n)
print(out)
fout.write(str(out))

