from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, out = 0, len(height) - 1, 0
        while (l < r):
            temp = height[l] - height[r]
            if out < (r - l) * (height[l] if temp < 0 else height[r]):
                out = (r - l) * (height[l] if temp < 0 else height[r]) 
            if temp < 0:
                l += 1
            else:
                r -= 1 
        return out

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")
a = [int(x) for x in fin.readline()[:-1].split(',')]
out = Solution().maxArea(a)
print(out)
fout.write(str(out))

