from typing import List
class Solution:
    def quicksort(l, r, obj):
        if (l >= r):
            return
        i, j, x = l, r, obj[r]
        while i < j:
            while i < j and obj[i] <= x:
                i += 1
            obj[j] = obj[i]
            while i < j and obj[j] > x:
                j -= 1
            obj[i] = obj[j]
        obj[i] = x
        Solution.quicksort(l, i - 1, obj)
        Solution.quicksort(i + 1, r, obj)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        last = len(nums) - 1
        Solution.quicksort(0, last, nums)
        out = nums[0] + nums[1] + nums[2]
        for i, x in enumerate(nums):
            j, k = i + 1, last
            if j >= k:
                return out
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if abs(out - target) > abs(temp - target):
                    out = temp
                if temp < target:
                    j += 1
                else:
                    k -= 1
        return out

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")
target = int(fin.readline()[:-1].split(' ')[1])
nums = [int(x) for x in fin.readline()[:-1].split(' ')]
out = Solution().threeSumClosest(nums, target)
print(out)
fout.write(str(out))

