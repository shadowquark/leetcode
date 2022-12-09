class Solution:
    def isValid(self, s: str) -> bool:
        lens = len(s)
        if lens & 1:
            return 0
        flag = []
        bra = [['(', ')'], ['[', ']'], ['{', '}']]
        for x in s:
            for y in bra:
                if x == y[0]:
                    flag.append(x)
                if x == y[1]:
                    if not len(flag) or flag[-1] != y[0]:
                        return 0
                    else:
                        flag = flag[:-1]                   
        if flag == []:
            return 1
        else:
            return 0

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")
s = fin.readline()[:-1]
out = Solution().isValid(s)
print(out)
fout.write(str(out))

