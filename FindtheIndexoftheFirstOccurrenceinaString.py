class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s1, s2 = haystack, needle
        for i in range(len(s1)):
            if len(s1) - len(s2) < i:
                return -1
            flag = 1
            for j in range(len(s2)):
                if s1[i + j] != s2[j]:
                    flag = 0
            if flag:
                return i
        return -1

fin = open("oo.xx", "r")
s1 = fin.readline()[:-1]
s2 = fin.readline()[:-1]
out = Solution().strStr(s1, s2)
print(out)

