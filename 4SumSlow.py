from typing import List
class Solution:
    def quicksort(l, r, obj):
        if not l < r:
            return obj
        i, j, x, = l, r, obj[r]
        while (i < j):
            while (i < j and obj[i] <= x):
                i += 1
            obj[j] = obj[i]
            while (i < j and obj[j] > x):
                j -= 1
            obj[i] = obj[j]
        obj[i] = x
        Solution.quicksort(l, i - 1, obj)
        Solution.quicksort(i + 1, r, obj)
        return obj
    def dfs(self, l1, r1):
        if not r1 - l1 > 2:
            return []
        l2, r2, out = l1 + 1, r1 - 1, []
        while l2 < r2:
            if self.nums[l1] + self.nums[l2] + self.nums[r2] + self.nums[r1] == self.target:
                out.append([self.nums[l1], self.nums[l2], self.nums[r2], self.nums[r1]])
                l2, r2 = l2 + 1, r2 - 1
                while l2 < r2 and self.nums[l2] == self.nums[l2 - 1]:
                    l2 += 1
                while l2 < r2 and self.nums[r2] == self.nums[r2 + 1]:
                    r2 -= 1
            elif self.nums[l1] + self.nums[l2] + self.nums[r2] + self.nums[r1] < self.target: 
                l2 += 1
                while l2 < r2 and self.nums[l2] == self.nums[l2 - 1]:
                    l2 += 1
            else:
                r2 -= 1
                while l2 < r2 and self.nums[r2] == self.nums[r2 + 1]:
                    r2 -= 1
        if self.nums[l1] + self.nums[l2] + self.nums[r2] + self.nums[r1] == self.target:
            out += self.dfs(l1 + 1, r1)
            out += self.dfs(l1, r1 - 1)
            l1, r1 = l1 + 1, r1 - 1
            while r1 - l1 > 2 and self.nums[l1] == self.nums[l1 - 1]:
                l1 += 1
            while r1 - l1 > 2 and self.nums[r1] == self.nums[r1 + 1]:
                r1 -= 1
        elif self.nums[l1] + self.nums[l2] + self.nums[r2] + self.nums[r1] < self.target:
            out += self.dfs(l1 + 1, l1 + 2, r2, r1)
            l1 += 1
            while r1 - l1 > 2 and self.nums[l1] == self.nums[l1 - 1]:
                l1 += 1
        else:
            r1 -= 1
            while r1 - l1 > 2 and self.nums[r1] == self.nums[r1 + 1]:
                r1 -= 1
        l2, r2 = l1 + 1, r1 - 1
        return out
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        lens, self.target = len(nums), target
        self.nums = Solution.quicksort(0, lens - 1, nums)
        return self.dfs(0, 1, lens - 2, lens - 1)
#       l1, l2, r1, r2 = 0, 1, lens - 1, lens - 2
#       while r1 - l1 > 2:
#           print(l1, l2, r2, r1)
#           while l2 < r2:
#               if nums[l1] + nums[l2] + nums[r2] + nums[r1] == target:
#                   out.append([nums[l1], nums[l2], nums[r2], nums[r1]])
#                   l2, r2 = l2 + 1, r2 - 1
#                   while l2 < r2 and nums[l2] == nums[l2 - 1]:
#                       l2 += 1
#                   while l2 < r2 and nums[r2] == nums[r2 + 1]:
#                       r2 -= 1
#               elif nums[l1] + nums[l2] + nums[r2] + nums[r1] < target: 
#                   l2 += 1
#                   while l2 < r2 and nums[l2] == nums[l2 - 1]:
#                       l2 += 1
#               else:
#                   r2 -= 1
#                   while l2 < r2 and nums[r2] == nums[r2 + 1]:
#                       r2 -= 1
#           if nums[l1] + nums[l2] + nums[r2] + nums[r1] < target:
#               l1 += 1
#               while r1 - l1 > 2 and nums[l1] == nums[l1 - 1]:
#                   l1 += 1
#           else:
#               r1 -= 1
#               while r1 - l1 > 2 and nums[r1] == nums[r1 + 1]:
#                   r1 -= 1
#           l2, r2 = l1 + 1, r1 - 1
#       return out
                
                
#       for i in range(lens - 3):
#           if i and nums[i] == nums[i - 1]:
#               continue
#           for j in range(i + 1, lens - 2):
#               if j - i - 1 and nums[j] == nums[j - 1]:
#                   continue
#               for k in range(j + 1, lens - 1):
#                   if k - j - 1 and nums[k] == nums[k - 1]:
#                       continue
#                   for kk in range(k + 1, lens):
#                       if kk - k - 1 and nums[kk] == nums[kk - 1]:
#                           continue
#                       if nums[i] + nums[j] + nums[k] + nums[kk] == target:
#                           out.append([nums[i], nums[j], nums[k], nums[kk]])
#                       if nums[i] + nums[j] + nums[k] + nums[kk] > target:
#                           break
#                   if nums[k] > 0 and nums[i] + nums[j] + nums[k] > target:
#                       break
#               if nums[j] > 0 and nums[i] + nums[j] > target:
#                   break
#           if nums[i] > 0 and nums[i] > target:
#               break
#       return out

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")
n = int(fin.readline()[:-1])
nums = [int(x) for x in fin.readline()[:-1].split(',')]
print(n, nums)
out = Solution().fourSum(nums, n)
for x in out:
    print(x)
    fout.write(str(x))

