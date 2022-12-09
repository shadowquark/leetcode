class Solution:
    def romanToInt(self, s: str) -> int:
        num =  {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        pos =  {'I': 0, 'V': 1, 'X': 2, 'L': 3, 'C': 4, 'D': 5, 'M': 6}
        out = 0
        for i, x in enumerate(s[::-1]):
            base = 1
            if i and pos[x] < pos[s[-i]]:
                base = -1
            out += base * num[x]
        return out
    
fin = open("oo.xx", "r")
fout = open("xx.oo", "w")

s = fin.readline()[:-1]
out = Solution().romanToInt(s)
print(out)
fout.write(str(out))

