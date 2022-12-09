from typing import List
class Solution:
    def dfs(n):
        if n = 0:
            return ')'
    def generateParenthesis(self, n: int) -> List[str]:
        out = Solution.dfs(n)
        return '(', 

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")

n = int(fin.readline())
out = Solution().generateParenthesis(n)
for x in out:
    print(x)
    fout.write(x)

