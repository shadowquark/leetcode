from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            else:
                pos += 1
                nums[pos] = nums[i]
        return pos + 1

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")
nums = [int(x) for x in fin.readline().split(',')]
out = Solution().removeDuplicates(nums)
print(out)
fout.write(str(out))

