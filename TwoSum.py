from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return i, j

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")
nums = [int(x) for x in fin.readline().split(',')]
target = int(fin.readline())
out = Solution().twoSum(nums, target)
print(out)
fout.write(str(out))

