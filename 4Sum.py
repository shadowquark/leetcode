from typing import List
import bisect
class Solution:
    def check(self, l, r):
        out, ll, rr = [], l + 1, r - 1
        while ll < rr:
            if (self.nums[l] + self.nums[ll] + self.nums[rr] + self.nums[r]
                == self.target):
                out.append([self.nums[l], self.nums[ll],
                            self.nums[rr], self.nums[r]])
                ll = bisect.bisect(self.nums, self.nums[ll], ll, rr)
                rr = bisect.bisect_left(self.nums, self.nums[rr], ll, rr) - 1
            elif (self.nums[l] + self.nums[ll] + self.nums[rr] + self.nums[r]
                    < self.target):
                ll = bisect.bisect(self.nums, self.nums[ll], ll, rr)
            else:
                rr = bisect.bisect_left(self.nums, self.nums[rr], ll, rr) - 1
        return out
        
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.nums, self.target, out, l, r = nums, target, [], 0, len(nums) - 1
        self.nums.sort()
        print(nums)
        while r - l > 2:
            out += self.check(l, r)
            ll = lll = bisect.bisect(self.nums, self.nums[l], l, r)
            while lll < r:
                out += self.check(lll, r)
                lll = bisect.bisect(self.nums, self.nums[lll], lll, r)
            rr = rrr = bisect.bisect_left(self.nums, self.nums[r], l, r) - 1
            while l < rrr:
                out += self.check(l, rrr)
                rrr = bisect.bisect_left(self.nums, self.nums[rrr], l, rrr) - 1
            l, r = ll, rr
        return out

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")
n = int(fin.readline())
nums = [int(x) for x in fin.readline().split(',')]
print(n, nums)
out = Solution().fourSum(nums, n)
for x in out:
    print(x)
    fout.write(str(x))

