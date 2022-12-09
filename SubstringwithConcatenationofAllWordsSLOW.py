from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        out, convert1 = [], []
        lens, lenWord, lenWords = len(s), len(words[0]), len(words)
        pos, token, nums = 0, {}, {}
        words.sort()
        for i in range(lenWords):
            if i and words[i] != words[i - 1]:
                pos += 1
            token[words[i]] = pos
            if words[i] in nums:
                nums[words[i]] += 1
            else:
                nums[words[i]] = 1
        jump = 0
        for i in range(lens - lenWord + 1):
            flag = [1 for _ in range(lenWords)]
            for j in range(lenWord):
                for k in range(lenWords):
                    if s[i + j] != words[k][j]:
                        flag[k] = 0
            pos = -1
            for x, y in enumerate(flag):
                if y == 1:
                    pos = x
            if jump:
                convert1.append(s[i])
                jump -= 1
            elif pos == -1:
                convert1.append(s[i])
            else:
                convert1.append(token[words[pos]])
                jump = lenWord - 1
            
        convert2, record, jump = [], [], 0
        for i, x in enumerate(convert1):
            if type(x) == int:
                convert2.append(x)
                record.append(i)
                jump = lenWord
            if jump:
                jump -= 1
            else:
                convert2.append(x)
                record.append(i)
        print(convert2)
        counts = [0 for _ in range(len(token))]
        for i, x in enumerate(token):
            counts[i] = nums[x]
        for i in range(len(convert2) - lenWords + 1):
            temp = convert2[i: i + lenWords]
            flag = 0
            for x in temp:
                if type(x) != int:
                    flag = 1
            if flag:
                continue
            check = [0 for _ in range(len(token))]
            for x in temp:
                check[x] += 1
            flag = 1
            for j, x in enumerate(check):
                if x != counts[j]:
                    flag = 0
            if flag:
                out.append(record[i])
        return out

fin = open("oo.xx", "r")
s = fin.readline()[:-1]
n = int(fin.readline())
words = []
for _ in range(n):
    words.append(fin.readline()[:-1])
out = Solution().findSubstring(s, words)
print(out)

