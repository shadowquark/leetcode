from typing import List
class Solution:
    def dfs(self, l, r, exp):
        if l == self.n and r == self.n:
            self.out.append(exp)
        maxl = self.n - l
        maxr = min(l - r, self.n - r)
        if maxl:
            exp += '('
            self.dfs(l + 1, r, exp)
            exp = exp[:-1]
        if maxr:
            exp += ')'
            self.dfs(l, r + 1, exp)
            exp = exp[:-1]
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.out = []
        self.dfs(0, 0, '')
        print(self.out)
        return self.out

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")

n = int(fin.readline())
out = Solution().generateParenthesis(n)
for x in out:
    print(x)
    fout.write(x)

