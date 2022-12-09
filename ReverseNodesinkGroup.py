from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def reverse(begin, end):
        previous = begin
        begin = end
        end = end.next
        head = previous
        tail = previous.next
        temp = 0
        while tail != end:
            forward = tail.next
            tail.next = head
            head = tail
            tail = forward
            temp += 1
            if temp == 10:
                break
        previous.next = end
        return begin, end, previous
    def reverseKGroup(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        tail, tot = head, 0
        while tail:
            tot += 1
            if tot == k:
                out = tail
            tail = tail.next
        if tot < k:
            return head
        begin, end = head, out
        printList(out)
        begin, end, previous = Solution.reverse(begin, end)
        printList(out)
        while 1:
            begin = end
            tail, tot = end, 0
            while tail:
                tot += 1
                if tot == k:
                    end = tail
                tail = tail.next
            if tot < k:
                return out
            previous.next = end
            printList(out)
            begin, end, previous = Solution.reverse(begin, end)
            printList(out)

def printList(x):
    temp = x
    tot = 0
    while temp:
        tot += 1
#       print(x.val)
        temp = temp.next
    print(tot, -1)

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")

k = int(fin.readline())
print(k, -1)
line = [int(x) for x in fin.readline().split(',')]
print(len(line))
head = tail = ListNode()
for x in line:
    tail.next = ListNode(x)
    tail = tail.next
head = head.next
out = Solution().reverseKGroup(head, k)
tot = 0
while out:
    tot += 1
#   print(out.val)
#   fout.write(str(out.val))
    out = out.next
print(tot, tot)

