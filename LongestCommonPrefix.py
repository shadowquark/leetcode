from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ''
        shortest = 200
        for x in strs:
            if x == '':
                return ''
            if len(x) < shortest:
                shortest = len(x)
        last, flag  = 0, 1
        while flag:
            test = strs[0][last]
            for x in strs:
                if x[last] != test:
                    flag = 0
            if flag and last + 1 == shortest:
                return strs[0][:shortest]
            elif flag:
                last += 1
            else:
                return strs[0][:last]

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")

strs = fin.readline()[:-1].split(',')
out = Solution().longestCommonPrefix(strs)
print(out)
fout.write(out)

