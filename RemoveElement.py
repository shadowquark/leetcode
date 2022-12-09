from typing import List
class Solution:
   def removeElement(self, nums: List[int], val: int) -> int: 
        pos = 0
        for x in nums:
            if x - val:
                nums[pos] = x
                pos += 1
        return pos

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")
val = int(fin.readline())
nums = [int(x) for x in fin.readline().split(',')]
out = Solution().removeElement(nums, val)
print(out)
fout.write(str(out))

