import functools as ft
def F(*z):
    z = [*z]
    return [*ft.reduce(lambda x, y: map(y, x), [z[:1]] + z[1:])][0]
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxR = maxP = 0 
        global_max, ss, out = 1, '\n', s[0]
        for x in s:
            ss += x + '\n'
        tot_len = len(ss)
        max_len = [0] * tot_len
        for i in range(1, tot_len):
            if i + global_max > tot_len:
                break
            r = 0
            if i - maxP > maxR:
                maxR, maxP = 0, i
            if maxR and max_len[2 * maxP - i] != maxP + maxR - i:
                continue
            else:
                r = maxP + maxR - i
            while i - r >= 0 and i + r < tot_len\
                    and ss[i + r] == ss[i - r]:
                r += 1
            r -= 1
            max_len[i] = r
            if r > maxR:
                maxP, maxR = i, r
            if r > global_max:
                global_max, out = r, ss[i - r : i + r + 1].replace('\n', '')
        return out

fin = open("oo.xx", 'r')
fout = open("xx.oo", 'w')

s = fin.readline()
F(s, Solution().longestPalindrome, fout.write)

fout.close()

