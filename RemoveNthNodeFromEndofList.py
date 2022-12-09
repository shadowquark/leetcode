from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        tail = head
        a = []
        while tail:
            a.append(tail.val)
            tail = tail.next
        a.pop(-n)
        if not a:
            return None
        tail = head
        pos = 0
        while tail:
            tail.val = a[pos]
            pos += 1
            if pos == len(a):
                tail.next = None
            tail = tail.next
        return head

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")

n = int(fin.readline())
a = [int(x) for x in fin.readline().split(',')]
print(n, a)
head = tail = ListNode(a[0])
for i in range(1, len(a)):
    tail.next = ListNode(a[i])
    tail = tail.next
out = Solution().removeNthFromEnd(head, n)
tail = head
while tail:
    print(tail.val)
    fout.write(str(tail.val))
    tail = tail.next

