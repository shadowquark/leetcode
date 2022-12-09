from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        pair1, pair2, tail = head, head.next, head.next.next
        head, previous = head.next, None
        while 1:
            pair2.next = pair1
            pair1.next = tail
            if previous:
                previous.next = pair2
            previous = pair1
            pair1 = tail
            if tail and tail.next:
                pair2 = tail.next
            else:
                return head
            tail = pair2.next

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")

line = [int(x) for x in fin.readline().split(',')]
head = tail = ListNode()
for x in line:
    tail.next = ListNode(x)
    tail = tail.next
head = head.next
out = Solution().swapPairs(head)
while out:
    print(out.val)
    fout.write(str(out.val))
    out = out.next

