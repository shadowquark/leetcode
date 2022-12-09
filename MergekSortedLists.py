from typing import Optional
from typing import List
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        lists.sort(key = lambda x: x.val if x else 10001)
        print(lists)
        if not lists:
            return None
        if not lists[0]:
            return None
        while lists[-1] == None:
            lists = lists[:-1]
        head = tail = ListNode()
        while lists:
            if (len(lists) == 1):
                tail.next = lists[0]
                return head.next
            while lists[0].val <= lists[1].val:
                tail.next = lists[0]
                tail = tail.next
                lists[0] = lists[0].next
                if not lists[0]:
                    break
            if not lists[0]:
                lists = lists[1:]
                continue
            else: 
                if lists[0].val >= lists[-1].val:
                    lists = lists[1:] + lists[:1]
                else:
                    l, r = 1, len(lists) - 1
                    while l < r:
                        if lists[0].val < lists[(l + r) // 2].val:
                            r = (l + r) // 2
                        else:
                            l = (l + r) // 2 + 1
                    lists.insert(l, lists[0])
                    lists = lists[1:]
        return head.next
fin = open("oo.xx", "r")
fout = open("xx.oo", "w")
k = int(fin.readline())
a = []
for _ in range(k):
    a.append([int(x) for x in fin.readline().split(',')])
a.append([])
a.append(None)
def convert(x):
    if not x:
        return None
    else:
        tempH = tempT = ListNode()
        for num in x:
            tempT.next = ListNode(num)
            tempT = tempT.next
        return tempH.next
lists = []
for x in a:
    lists.append(convert(x))
out = Solution().mergeKLists(lists)
while out:
    print(out.val)
    fout.write(str(out.val))
    out = out.next

